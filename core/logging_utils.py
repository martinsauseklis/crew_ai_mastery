"""Logging utilities for the AI Mastery Platform."""

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime

from .config import Config


def setup_logging(crew_name: Optional[str] = None, level: Optional[str] = None) -> logging.Logger:
    """
    Set up structured logging for a crew or the main application.

    Args:
        crew_name: Name of the crew (creates separate log file)
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Configured logger instance
    """
    log_level = level or Config.LOG_LEVEL
    logger_name = crew_name or "ai_mastery_platform"

    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, log_level.upper()))

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Console handler with simple format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # File handler with detailed format
    if crew_name:
        log_file = Config.LOGS_DIR / f"{crew_name}.log"
    else:
        log_file = Config.LOGS_DIR / "main.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(getattr(logging, log_level.upper()))
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name: Logger name (typically crew or module name)

    Returns:
        Logger instance
    """
    return logging.getLogger(name)


class TaskLogger:
    """Context manager for logging task execution."""

    def __init__(self, logger: logging.Logger, task_name: str, crew_name: str):
        self.logger = logger
        self.task_name = task_name
        self.crew_name = crew_name
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        self.logger.info(f"Starting task: {self.task_name} in {self.crew_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = (datetime.now() - self.start_time).total_seconds()
        if exc_type is None:
            self.logger.info(
                f"Completed task: {self.task_name} in {duration:.2f}s"
            )
        else:
            self.logger.error(
                f"Failed task: {self.task_name} after {duration:.2f}s - {exc_val}"
            )
        return False  # Don't suppress exceptions
