"""Platform Crew - Phase 3: Product & Platform Build."""

import uuid
import time
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging
from core.state_manager import TaskStatus
from core.config import Config
from agents import (
    create_ux_designer,
    create_fullstack_developer,
    create_backend_engineer,
    create_ml_engineer,
    create_llm_engineer
)
from tasks import get_platform_tasks


def run_platform_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Platform Crew for Phase 3: Product & Platform Build.

    This crew designs UX, system architecture, data infrastructure,
    ML systems, LLM integration, and creates the MVP implementation plan.

    Args:
        state_manager: StateManager instance for checkpointing
        llm_client: LLMClient instance for cost tracking

    Returns:
        Dictionary with execution results
    """
    crew_name = "PlatformCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        ux_designer = create_ux_designer(llm_client)
        fullstack_dev = create_fullstack_developer(llm_client)
        backend_engineer = create_backend_engineer(llm_client)
        ml_engineer = create_ml_engineer(llm_client)
        llm_engineer = create_llm_engineer(llm_client)

        # Create tasks
        logger.info("Creating tasks...")
        tasks = get_platform_tasks(
            ux_designer,
            fullstack_dev,
            backend_engineer,
            ml_engineer,
            llm_engineer
        )

        # Check for completed tasks (resumability)
        task_ids = [
            "platform_ux_design",
            "platform_system_architecture",
            "platform_data_infrastructure",
            "platform_ml_systems",
            "platform_llm_integration",
            "platform_mvp_plan"
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
                ux_designer,
                fullstack_dev,
                backend_engineer,
                ml_engineer,
                llm_engineer
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

        # Mark phase as in progress
        state_manager.set_phase_status(3, "Product & Platform Build", TaskStatus.IN_PROGRESS)

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
        state_manager.set_phase_status(3, "Product & Platform Build", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(3, "Product & Platform Build", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
