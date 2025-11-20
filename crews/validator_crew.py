"""Validator Crew for testing and debugging the AI Mastery Platform"""

import uuid
import time
from pathlib import Path
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging, get_logger
from core.state_manager import TaskStatus
from core.config import Config
from demo_config import DemoConfig
from agents.validator_agents import (
    create_backend_validator,
    create_frontend_validator,
    create_integration_validator,
    create_data_validator,
    create_debug_assistant
)
from tasks.validator_tasks import get_validator_tasks


def run_validator_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Validator Crew to test the platform and generate fixes.

    This crew tests backend, frontend, integration, and data quality,
    then generates actionable fixes for all issues found.
    """
    crew_name = "ValidatorCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create validator agents
        logger.info("Creating validator agents...")
        backend_validator = create_backend_validator(llm_client)
        frontend_validator = create_frontend_validator(llm_client)
        integration_validator = create_integration_validator(llm_client)
        data_validator = create_data_validator(llm_client)
        debug_assistant = create_debug_assistant(llm_client)

        logger.info("✓ Created 5 validator agents")

        # Create validation tasks
        logger.info("Creating validation tasks...")
        tasks = get_validator_tasks(
            backend_validator,
            frontend_validator,
            integration_validator,
            data_validator,
            debug_assistant
        )

        logger.info(f"✓ Created {len(tasks)} validation tasks")

        # Task IDs for tracking
        task_ids = [
            "validate_backend",
            "validate_frontend",
            "validate_integration",
            "validate_data",
            "generate_fixes"
        ]

        for i, task_id in enumerate(task_ids):
            state_manager.set_task_status(
                crew_name,
                task_id,
                TaskStatus.PENDING,
                task_name=tasks[i].description[:50]
            )

        # Create and run validation crew
        logger.info("Initializing validation crew...")
        crew = Crew(
            agents=[
                backend_validator,
                frontend_validator,
                integration_validator,
                data_validator,
                debug_assistant
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=Config.CREW_VERBOSE
        )

        state_manager.set_phase_status(6, "Platform Validation & Debug", TaskStatus.IN_PROGRESS)

        logger.info("Executing validation tasks...")
        logger.info("This will generate 5 validation reports in artifacts/demo/")
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

        state_manager.set_phase_status(6, "Platform Validation & Debug", TaskStatus.COMPLETED)
        state_manager.complete_crew_run(run_id)

        logger.info(f"{crew_name} completed successfully")

        # Print summary
        print("\n" + "="*60)
        print("VALIDATION COMPLETE - REPORTS GENERATED")
        print("="*60)
        print("\nValidation Reports:")
        print("  1. backend_validation_report.md")
        print("  2. frontend_validation_report.md")
        print("  3. integration_validation_report.md")
        print("  4. data_validation_report.md")
        print("  5. platform_fixes_plan.md (← START HERE for fixes)")
        print("\nLocation: artifacts/demo/")
        print("\nNext Steps:")
        print("  1. Review platform_fixes_plan.md")
        print("  2. Apply critical fixes first")
        print("  3. Re-run validators to verify fixes")
        print("="*60 + "\n")

        return {
            "status": "success",
            "crew_name": crew_name,
            "run_id": run_id,
            "result": str(result),
            "reports_generated": 5
        }

    except Exception as e:
        logger.error(f"{crew_name} failed: {str(e)}", exc_info=True)
        state_manager.complete_crew_run(run_id, error_message=str(e))
        state_manager.set_phase_status(6, "Platform Validation & Debug", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
