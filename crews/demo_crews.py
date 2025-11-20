"""Demo Crews - All 4 phases with simplified tasks for demo mode."""

import uuid
import time
from pathlib import Path
from crewai import Crew, Process
from core import StateManager, LLMClient, setup_logging, get_logger
from core.state_manager import TaskStatus
from core.config import Config
from demo_config import DemoConfig
from agents import (
    create_chief_of_staff,
    create_product_manager,
    create_curriculum_architect,
    create_ai_sme,
    create_instructional_designer,
    create_cognitive_scientist,
    create_behavior_designer,
    create_ux_designer,
    create_fullstack_developer,
    create_backend_engineer,
    create_ml_engineer,
    create_llm_engineer,
    create_qa_researcher,
    create_implementation_architect,
    create_backend_implementer,
    create_frontend_implementer,
    create_devops_implementer
)
from tasks.demo_tasks import (
    get_demo_strategy_tasks,
    get_demo_curriculum_tasks,
    get_demo_platform_tasks,
    get_demo_qa_tasks
)
from tasks.demo_implementation_tasks import get_demo_implementation_tasks


def should_skip_task_by_artifact(task, logger) -> bool:
    """
    Check if task should be skipped because artifact already exists.

    Args:
        task: CrewAI Task object
        logger: Logger instance

    Returns:
        True if task should be skipped, False otherwise
    """
    if task.output_file:
        artifact_path = Path(task.output_file)
        if artifact_path.exists() and artifact_path.stat().st_size > 100:  # At least 100 bytes
            logger.info(f"Skipping task - artifact already exists: {artifact_path.name}")
            return True
    return False


def filter_tasks(tasks, logger):
    """
    Filter out tasks that already have artifacts generated.

    Args:
        tasks: List of CrewAI Task objects
        logger: Logger instance

    Returns:
        Tuple of (tasks_to_run, skipped_count)
    """
    tasks_to_run = []
    skipped_count = 0

    for task in tasks:
        if should_skip_task_by_artifact(task, logger):
            skipped_count += 1
        else:
            tasks_to_run.append(task)

    return tasks_to_run, skipped_count


def run_demo_strategy_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Strategy Crew (DEMO) for Phase 1: Vision & Requirements.

    Uses simplified tasks with reduced output expectations.
    """
    crew_name = "DemoStrategyCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents (same as production)
        logger.info("Creating agents...")
        chief_of_staff = create_chief_of_staff(llm_client)
        product_manager = create_product_manager(llm_client)

        # Override max_iterations for demo
        chief_of_staff.max_iter = DemoConfig.DEMO_MAX_ITERATIONS
        product_manager.max_iter = DemoConfig.DEMO_MAX_ITERATIONS

        # Create demo tasks
        logger.info("Creating demo tasks...")
        all_tasks = get_demo_strategy_tasks(chief_of_staff, product_manager)

        # Filter tasks that already have artifacts
        tasks_to_run, skipped_count = filter_tasks(all_tasks, logger)

        if skipped_count > 0:
            logger.info(f"Skipped {skipped_count} task(s) with existing artifacts")

        if not tasks_to_run:
            logger.info("All tasks already completed. Skipping crew execution.")
            state_manager.set_phase_status(1, "Demo: Vision & Requirements", TaskStatus.COMPLETED)
            return {
                "status": "success",
                "crew_name": crew_name,
                "run_id": run_id,
                "result": "All tasks already completed (artifacts exist)",
                "skipped": True
            }

        # Task IDs for tracking
        task_ids = [
            "demo_strategy_define_objectives",
            "demo_strategy_create_prd",
            "demo_strategy_create_roadmap"
        ]

        for i, task_id in enumerate(task_ids):
            state_manager.set_task_status(
                crew_name,
                task_id,
                TaskStatus.PENDING,
                task_name=all_tasks[i].description[:50]
            )

        # Create and run crew
        logger.info(f"Initializing crew with {len(tasks_to_run)} task(s)...")
        crew = Crew(
            agents=[chief_of_staff, product_manager],
            tasks=tasks_to_run,
            process=Process.sequential,
            verbose=Config.CREW_VERBOSE
        )

        # Mark phase as in progress
        state_manager.set_phase_status(1, "Demo: Vision & Requirements", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
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

        state_manager.set_phase_status(1, "Demo: Vision & Requirements", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(1, "Demo: Vision & Requirements", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }


def run_demo_curriculum_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Curriculum Crew (DEMO) for Phase 2: Curriculum Construction.

    Uses simplified tasks with reduced output expectations.
    """
    crew_name = "DemoCurriculumCrew"
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

        # Override max_iterations for demo
        for agent in [curriculum_architect, ai_sme, instructional_designer, cognitive_scientist, behavior_designer]:
            agent.max_iter = DemoConfig.DEMO_MAX_ITERATIONS

        # Create demo tasks
        logger.info("Creating demo tasks...")
        tasks = get_demo_curriculum_tasks(
            curriculum_architect,
            ai_sme,
            instructional_designer,
            cognitive_scientist,
            behavior_designer
        )

        task_ids = [
            "demo_curriculum_scaffold",
            "demo_technical_validation",
            "demo_learning_science",
            "demo_instructional_content",
            "demo_engagement_systems"
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
            agents=[curriculum_architect, ai_sme, instructional_designer, cognitive_scientist, behavior_designer],
            tasks=tasks,
            process=Process.sequential,
            verbose=Config.CREW_VERBOSE
        )

        state_manager.set_phase_status(2, "Demo: Curriculum Construction", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
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

        state_manager.set_phase_status(2, "Demo: Curriculum Construction", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(2, "Demo: Curriculum Construction", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }


def run_demo_platform_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Platform Crew (DEMO) for Phase 3: Product & Platform Build.

    Uses simplified tasks with reduced output expectations.
    """
    crew_name = "DemoPlatformCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        ux_designer = create_ux_designer(llm_client)
        fullstack_developer = create_fullstack_developer(llm_client)
        backend_engineer = create_backend_engineer(llm_client)
        ml_engineer = create_ml_engineer(llm_client)
        llm_engineer = create_llm_engineer(llm_client)

        # Override max_iterations for demo
        for agent in [ux_designer, fullstack_developer, backend_engineer, ml_engineer, llm_engineer]:
            agent.max_iter = DemoConfig.DEMO_MAX_ITERATIONS

        # Create demo tasks
        logger.info("Creating demo tasks...")
        tasks = get_demo_platform_tasks(
            ux_designer,
            fullstack_developer,
            backend_engineer,
            ml_engineer,
            llm_engineer
        )

        task_ids = [
            "demo_platform_ux_design",
            "demo_platform_system_architecture",
            "demo_platform_data_infrastructure",
            "demo_platform_ml_systems",
            "demo_platform_llm_integration",
            "demo_platform_mvp_plan"
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
            agents=[ux_designer, fullstack_developer, backend_engineer, ml_engineer, llm_engineer],
            tasks=tasks,
            process=Process.sequential,
            verbose=Config.CREW_VERBOSE
        )

        state_manager.set_phase_status(3, "Demo: Product & Platform Build", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
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

        state_manager.set_phase_status(3, "Demo: Product & Platform Build", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(3, "Demo: Product & Platform Build", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }


def run_demo_qa_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the QA Crew (DEMO) for Phase 4: Testing & Refinement.

    Uses simplified tasks with reduced output expectations.
    """
    crew_name = "DemoQACrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agent
        logger.info("Creating agent...")
        qa_researcher = create_qa_researcher(llm_client)

        # Override max_iterations for demo
        qa_researcher.max_iter = DemoConfig.DEMO_MAX_ITERATIONS

        # Create demo tasks
        logger.info("Creating demo tasks...")
        tasks = get_demo_qa_tasks(qa_researcher)

        task_ids = [
            "demo_qa_comprehensive_review",
            "demo_qa_refinement_backlog",
            "demo_qa_validation_framework"
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
            verbose=Config.CREW_VERBOSE
        )

        state_manager.set_phase_status(4, "Demo: Testing & Refinement", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
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

        state_manager.set_phase_status(4, "Demo: Testing & Refinement", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(4, "Demo: Testing & Refinement", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }


def run_demo_implementation_crew(state_manager: StateManager, llm_client: LLMClient) -> dict:
    """
    Run the Implementation Crew (DEMO) for Phase 5: Platform Implementation.

    Actually builds the platform code based on the design artifacts.
    """
    crew_name = "DemoImplementationCrew"
    logger = setup_logging(crew_name)
    run_id = f"{crew_name}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting {crew_name} (Run ID: {run_id})")
    state_manager.start_crew_run(crew_name, run_id)

    try:
        # Create agents
        logger.info("Creating agents...")
        implementation_architect = create_implementation_architect(llm_client)
        backend_implementer = create_backend_implementer(llm_client)
        frontend_implementer = create_frontend_implementer(llm_client)
        devops_implementer = create_devops_implementer(llm_client)

        # Override max_iterations for demo
        for agent in [implementation_architect, backend_implementer, frontend_implementer, devops_implementer]:
            agent.max_iter = DemoConfig.DEMO_MAX_ITERATIONS

        # Create demo tasks
        logger.info("Creating demo tasks...")
        all_tasks = get_demo_implementation_tasks(
            implementation_architect,
            backend_implementer,
            frontend_implementer,
            devops_implementer
        )

        # Filter tasks that already have artifacts
        tasks_to_run, skipped_count = filter_tasks(all_tasks, logger)

        if skipped_count > 0:
            logger.info(f"Skipped {skipped_count} task(s) with existing artifacts")

        if not tasks_to_run:
            logger.info("All tasks already completed. Skipping crew execution.")
            state_manager.set_phase_status(5, "Demo: Platform Implementation", TaskStatus.COMPLETED)
            return {
                "status": "success",
                "crew_name": crew_name,
                "run_id": run_id,
                "result": "All tasks already completed (artifacts exist)",
                "skipped": True
            }

        task_ids = [
            "demo_implementation_plan",
            "demo_backend_implementation",
            "demo_frontend_implementation",
            "demo_deployment_setup"
        ]

        for i, task_id in enumerate(task_ids):
            state_manager.set_task_status(
                crew_name,
                task_id,
                TaskStatus.PENDING,
                task_name=all_tasks[i].description[:50]
            )

        # Create and run crew
        logger.info(f"Initializing crew with {len(tasks_to_run)} task(s)...")
        crew = Crew(
            agents=[implementation_architect, backend_implementer, frontend_implementer, devops_implementer],
            tasks=tasks_to_run,
            process=Process.sequential,
            verbose=Config.CREW_VERBOSE
        )

        state_manager.set_phase_status(5, "Demo: Platform Implementation", TaskStatus.IN_PROGRESS)

        logger.info("Executing crew tasks...")
        time.sleep(Config.TASK_DELAY_SECONDS)

        result = crew.kickoff()

        # Mark tasks as completed
        for i, task_id in enumerate(task_ids):
            state_manager.set_task_status(
                crew_name,
                task_id,
                TaskStatus.COMPLETED,
                task_name=all_tasks[i].description[:50],
                artifacts_path=str(all_tasks[i].output_file) if all_tasks[i].output_file else None
            )

        state_manager.set_phase_status(5, "Demo: Platform Implementation", TaskStatus.COMPLETED)
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
        state_manager.set_phase_status(5, "Demo: Platform Implementation", TaskStatus.FAILED)
        return {
            "status": "failed",
            "crew_name": crew_name,
            "run_id": run_id,
            "error": str(e)
        }
