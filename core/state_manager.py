"""State management and checkpointing for crash recovery."""

import json
import sqlite3
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any

from .config import Config
from .logging_utils import get_logger

logger = get_logger(__name__)


class TaskStatus(Enum):
    """Task execution status."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class StateManager:
    """
    Manages persistent state for crew execution and task tracking.
    Enables crash recovery and resumability.
    """

    def __init__(self, db_path: Optional[Path] = None):
        """
        Initialize the StateManager.

        Args:
            db_path: Path to SQLite database (defaults to Config.STATE_DB_PATH)
        """
        self.db_path = db_path or Config.STATE_DB_PATH
        self._init_db()

    def _init_db(self):
        """Initialize the SQLite database schema."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Tasks table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    crew_name TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    task_name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    artifacts_path TEXT,
                    metadata TEXT,
                    UNIQUE(crew_name, task_id)
                )
            """)

            # Crew runs table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS crew_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    crew_name TEXT NOT NULL,
                    run_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    started_at TEXT NOT NULL,
                    completed_at TEXT,
                    error_message TEXT,
                    UNIQUE(run_id)
                )
            """)

            # Phase tracking table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS phases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phase_number INTEGER NOT NULL,
                    phase_name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    UNIQUE(phase_number)
                )
            """)

            conn.commit()
            logger.info(f"Initialized state database at {self.db_path}")

    def get_task_status(self, crew_name: str, task_id: str) -> Optional[TaskStatus]:
        """
        Get the current status of a task.

        Args:
            crew_name: Name of the crew
            task_id: Unique task identifier

        Returns:
            TaskStatus or None if task not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT status FROM tasks WHERE crew_name = ? AND task_id = ?",
                (crew_name, task_id)
            )
            result = cursor.fetchone()
            return TaskStatus(result[0]) if result else None

    def set_task_status(
        self,
        crew_name: str,
        task_id: str,
        status: TaskStatus,
        task_name: str = "",
        artifacts_path: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Set or update the status of a task.

        Args:
            crew_name: Name of the crew
            task_id: Unique task identifier
            status: New task status
            task_name: Human-readable task name
            artifacts_path: Path to task output artifacts
            metadata: Additional metadata as JSON
        """
        now = datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (crew_name, task_id, task_name, status, created_at, updated_at, artifacts_path, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(crew_name, task_id) DO UPDATE SET
                    status = excluded.status,
                    updated_at = excluded.updated_at,
                    artifacts_path = COALESCE(excluded.artifacts_path, artifacts_path),
                    metadata = COALESCE(excluded.metadata, metadata)
            """, (crew_name, task_id, task_name, status.value, now, now, artifacts_path, metadata_json))
            conn.commit()

        logger.info(f"Task {crew_name}/{task_id} status: {status.value}")

    def list_pending_tasks(self, crew_name: str) -> List[Dict[str, Any]]:
        """
        List all pending tasks for a crew.

        Args:
            crew_name: Name of the crew

        Returns:
            List of task dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tasks WHERE crew_name = ? AND status = ?",
                (crew_name, TaskStatus.PENDING.value)
            )
            return [dict(row) for row in cursor.fetchall()]

    def should_skip_task(self, crew_name: str, task_id: str) -> bool:
        """
        Check if a task should be skipped (already completed).

        Args:
            crew_name: Name of the crew
            task_id: Unique task identifier

        Returns:
            True if task is already completed
        """
        status = self.get_task_status(crew_name, task_id)
        return status == TaskStatus.COMPLETED

    def start_crew_run(self, crew_name: str, run_id: str):
        """
        Mark the start of a crew execution.

        Args:
            crew_name: Name of the crew
            run_id: Unique run identifier
        """
        now = datetime.now().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO crew_runs (crew_name, run_id, status, started_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(run_id) DO UPDATE SET
                    status = excluded.status,
                    started_at = excluded.started_at
            """, (crew_name, run_id, TaskStatus.IN_PROGRESS.value, now))
            conn.commit()

        logger.info(f"Started crew run: {crew_name} ({run_id})")

    def complete_crew_run(self, run_id: str, error_message: Optional[str] = None):
        """
        Mark the completion of a crew execution.

        Args:
            run_id: Unique run identifier
            error_message: Error message if run failed
        """
        now = datetime.now().isoformat()
        status = TaskStatus.FAILED.value if error_message else TaskStatus.COMPLETED.value

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE crew_runs
                SET status = ?, completed_at = ?, error_message = ?
                WHERE run_id = ?
            """, (status, now, error_message, run_id))
            conn.commit()

        logger.info(f"Completed crew run: {run_id} ({status})")

    def set_phase_status(self, phase_number: int, phase_name: str, status: TaskStatus):
        """
        Track phase-level progress.

        Args:
            phase_number: Phase number (1-4)
            phase_name: Human-readable phase name
            status: Phase status
        """
        now = datetime.now().isoformat()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if status == TaskStatus.IN_PROGRESS:
                cursor.execute("""
                    INSERT INTO phases (phase_number, phase_name, status, started_at)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(phase_number) DO UPDATE SET
                        status = excluded.status,
                        started_at = excluded.started_at
                """, (phase_number, phase_name, status.value, now))
            elif status == TaskStatus.COMPLETED:
                cursor.execute("""
                    UPDATE phases
                    SET status = ?, completed_at = ?
                    WHERE phase_number = ?
                """, (status.value, now, phase_number))
            conn.commit()

    def get_phase_status(self, phase_number: int) -> Optional[TaskStatus]:
        """Get the status of a phase."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT status FROM phases WHERE phase_number = ?",
                (phase_number,)
            )
            result = cursor.fetchone()
            return TaskStatus(result[0]) if result else None

    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of all tracked state.

        Returns:
            Dictionary with counts and status information
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Task counts by status
            cursor.execute("""
                SELECT status, COUNT(*) as count
                FROM tasks
                GROUP BY status
            """)
            task_counts = dict(cursor.fetchall())

            # Crew run counts
            cursor.execute("""
                SELECT status, COUNT(*) as count
                FROM crew_runs
                GROUP BY status
            """)
            run_counts = dict(cursor.fetchall())

            # Phase progress
            cursor.execute("SELECT * FROM phases ORDER BY phase_number")
            phases = [dict(zip([col[0] for col in cursor.description], row))
                     for row in cursor.fetchall()]

            return {
                "task_counts": task_counts,
                "run_counts": run_counts,
                "phases": phases
            }
