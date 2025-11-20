"""Curriculum Crew - Phase 2: Curriculum Construction."""

import uuid
import time
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging
from core.state_manager import TaskStatus
from core.config import Config
from agents import (
    create_curriculum_architect,
    create_ai_sme,
    create_instructional_designer,
    create_cognitive_scientist,
    create_behavior_designer
)
from tasks import get_curriculum_tasks


def run_curriculum_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Curriculum Crew for Phase 2: Curriculum Construction.

    This crew designs the curriculum structure, validates technical depth,
    applies learning science, creates instructional content, and designs
    engagement systems.

    Args:
        state_manager: StateManager instance for checkpointing
        llm_client: LLMClient instance for cost tracking

    Returns:
        Dictionary with execution results
    """
    crew_name = "CurriculumCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        curriculum_architect = create_curriculum_architect(llm_client)
        ai_sme = create_ai_sme(llm_client)
        instructional_designer = create_instructional_designer(llm_client)
        cognitive_scientist = create_cognitive_scientist(llm_client)
        behavior_designer = create_behavior_designer(llm_client)

        # Create tasks
        logger.info("Creating tasks...")
        tasks = get_curriculum_tasks(
            curriculum_architect,
            ai_sme,
            instructional_designer,
            cognitive_scientist,
            behavior_designer
        )

        # Check for completed tasks (resumability)
        task_ids = [
            "curriculum_scaffold",
            "technical_validation",
            "learning_science",
            "instructional_content",
            "engagement_systems"
        ]

        for i, task_id in enumerate(task_ids):
            if state_manager.should_skip_task(crew_name, task_id):
                logger.info(f"Skipping completed task: {task_id}")
            else:
                state_manager.set_task_status(
                    crew_name,
                    task_id,
                    TaskStatus.PENDING,
                    task_name=tasks[i].description[:50]
                )

        # Create and run crew
        logger.info("Initializing crew...")
        crew = Crew(
            agents=[
                curriculum_architect,
                ai_sme,
                instructional_designer,
                cognitive_scientist,
                behavior_designer
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

        # Mark phase as in progress
        state_manager.set_phase_status(2, "Curriculum Construction", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
        logger.info("Note: Rate limiting is active. The system will automatically pause if approaching API rate limits.")

        # Small delay before kickoff to help with rate limiting
        time.sleep(Config.TASK_DELAY_SECONDS)

        result = crew.kickoff()

        # Mark tasks as completed
        for i, task_id in enumerate(task_ids):
            state_manager.set_task_status(
                crew_name,
                task_id,
                TaskStatus.COMPLETED,
                task_name=tasks[i].description[:50],
                artifacts_path=str(tasks[i].output_file) if tasks[i].output_file else None
            )

        # Mark phase as completed
        state_manager.set_phase_status(2, "Curriculum Construction", TaskStatus.COMPLETED)
        state_manager.complete_crew_run(run_id)

        logger.info(f"{crew_name} completed successfully")
        return {
            "status": "success",
            "crew_name": crew_name,
            "run_id": run_id,
            "result": str(result)
        }

    except Exception as e:
        logger.error(f"{crew_name} failed: {str(e)}", exc_info=True)
        state_manager.complete_crew_run(run_id, error_message=str(e))
        state_manager.set_phase_status(2, "Curriculum Construction", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
