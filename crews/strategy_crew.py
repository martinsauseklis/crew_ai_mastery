"""Strategy Crew - Phase 1: Vision & Requirements."""

import uuid
import time
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging, get_logger
from core.state_manager import TaskStatus
from core.config import Config
from agents import create_chief_of_staff, create_product_manager
from tasks import get_strategy_tasks


def run_strategy_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Strategy Crew for Phase 1: Vision & Requirements.

    This crew defines learning objectives, creates the PRD, and establishes
    the product roadmap.

    Args:
        state_manager: StateManager instance for checkpointing
        llm_client: LLMClient instance for cost tracking

    Returns:
        Dictionary with execution results
    """
    crew_name = "StrategyCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        chief_of_staff = create_chief_of_staff(llm_client)
        product_manager = create_product_manager(llm_client)

        # Create tasks
        logger.info("Creating tasks...")
        tasks = get_strategy_tasks(chief_of_staff, product_manager)

        # Check for completed tasks (resumability)
        task_ids = [
            "strategy_define_objectives",
            "strategy_create_prd",
            "strategy_create_roadmap"
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
            agents=[chief_of_staff, product_manager],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

        # Mark phase as in progress
        state_manager.set_phase_status(1, "Vision & Requirements", TaskStatus.IN_PROGRESS)

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
        state_manager.set_phase_status(1, "Vision & Requirements", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(1, "Vision & Requirements", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
