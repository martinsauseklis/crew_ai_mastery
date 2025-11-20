"""QA Crew - Phase 4: Testing & Refinement."""

import uuid
import time
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging
from core.state_manager import TaskStatus
from core.config import Config
from agents import create_qa_researcher
from tasks import get_qa_tasks


def run_qa_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the QA Crew for Phase 4: Testing & Refinement.

    This crew conducts comprehensive review, creates a refinement backlog,
    and designs validation frameworks.

    Args:
        state_manager: StateManager instance for checkpointing
        llm_client: LLMClient instance for cost tracking

    Returns:
        Dictionary with execution results
    """
    crew_name = "QACrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        qa_researcher = create_qa_researcher(llm_client)

        # Create tasks
        logger.info("Creating tasks...")
        tasks = get_qa_tasks(qa_researcher)

        # Check for completed tasks (resumability)
        task_ids = [
            "qa_comprehensive_review",
            "qa_refinement_backlog",
            "qa_validation_framework"
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
            agents=[qa_researcher],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

        # Mark phase as in progress
        state_manager.set_phase_status(4, "Testing & Refinement", TaskStatus.IN_PROGRESS)

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
        state_manager.set_phase_status(4, "Testing & Refinement", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(4, "Testing & Refinement", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
