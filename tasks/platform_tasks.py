"""Tasks for the Platform Crew (Phase 3: Product & Platform Build)."""

from crewai import Task
from core.config import Config


def get_platform_tasks(
    ux_designer,
    fullstack_dev,
    backend_engineer,
    ml_engineer,
    llm_engineer
) -> list:
    """
    Get tasks for Phase 3: Product & Platform Build.

    Returns:
        List of CrewAI Task objects
    """
    artifacts_dir = Config.ARTIFACTS_DIR

    task_design_ux = Task(
        description=(
            "Design the user experience and interface for the AI Mastery Platform. Based on the PRD "
            "and instructional content plans, create:\n\n"
            "- Information architecture and navigation structure\n"
            "- Key user flows (onboarding, lesson consumption, practice, progress tracking)\n"
            "- Wireframes for critical screens (dashboard, lesson view, exercise interface, progress)\n"
            "- Design system foundations (typography, colors, spacing, components)\n"
            "- Responsive design considerations (desktop, tablet, mobile)\n"
            "- Accessibility guidelines\n\n"
            "Create a learning experience that feels effortless, engaging, and focused. Minimize cognitive "
            "friction while maximizing clarity and delight."
        ),
        expected_output=(
            "A markdown file 'ux_design.md' with:\n"
            "- Information architecture diagram (textual representation)\n"
            "- Detailed user flow descriptions\n"
            "- ASCII wireframes or detailed textual descriptions of key screens\n"
            "- Design system specification\n"
            "- Interaction patterns and micro-interactions\n"
            "- Mobile-first responsive considerations\n"
            "- Accessibility checklist (WCAG compliance)"
        ),
        agent=ux_designer,
        output_file=str(artifacts_dir / "ux_design.md")
    )

    task_create_system_architecture = Task(
        description=(
            "Design the technical architecture for the AI Mastery Platform. Create a comprehensive "
            "system design that covers:\n\n"
            "- Frontend architecture (React/Next.js, state management, routing)\n"
            "- Backend architecture (API design, services, authentication)\n"
            "- Database schema (users, progress, content, analytics)\n"
            "- Deployment architecture (hosting, CI/CD, monitoring)\n"
            "- Third-party integrations (LLM APIs, analytics, email)\n"
            "- Security and data privacy considerations\n\n"
            "Design for the MVP while laying foundations for future scale. Choose pragmatic, proven "
            "technologies. Document key architectural decisions and trade-offs."
        ),
        expected_output=(
            "A markdown file 'system_architecture.md' with:\n"
            "- High-level architecture diagram (textual/ASCII)\n"
            "- Technology stack decisions and rationale\n"
            "- Component architecture and data flow\n"
            "- API design and endpoint specifications\n"
            "- Database schema with entity relationships\n"
            "- Authentication and authorization strategy\n"
            "- Deployment and DevOps plan\n"
            "- Security and privacy measures"
        ),
        agent=fullstack_dev,
        output_file=str(artifacts_dir / "system_architecture.md"),
        context=[task_design_ux]
    )

    task_design_data_infrastructure = Task(
        description=(
            "Design the data infrastructure for learning analytics, progress tracking, and content delivery. "
            "Create detailed specifications for:\n\n"
            "- Database schema (PostgreSQL) for all entities\n"
            "- Data models for user progress and knowledge state\n"
            "- Content storage and delivery strategy\n"
            "- Learning analytics data pipeline\n"
            "- Event tracking and logging architecture\n"
            "- Data privacy and GDPR compliance\n\n"
            "Ensure the data layer supports both current MVP features and future ML-powered personalization."
        ),
        expected_output=(
            "A markdown file 'data_infrastructure.md' with:\n"
            "- Complete database schema (tables, columns, relationships, indexes)\n"
            "- Data models for progress tracking and skill mastery\n"
            "- Content delivery and caching strategy\n"
            "- Analytics event schema and pipeline design\n"
            "- API contracts for data operations\n"
            "- Data retention and privacy policies\n"
            "- Backup and disaster recovery plan"
        ),
        agent=backend_engineer,
        output_file=str(artifacts_dir / "data_infrastructure.md"),
        context=[task_create_system_architecture]
    )

    task_design_ml_systems = Task(
        description=(
            "Design machine learning systems for personalization and adaptive learning. While the MVP "
            "may use simple heuristics, plan the ML infrastructure for:\n\n"
            "- Content recommendation engine (similar to Netflix/Spotify)\n"
            "- Difficulty adjustment and adaptive learning paths\n"
            "- Knowledge tracing and skill mastery prediction\n"
            "- Learning analytics and insight generation\n\n"
            "Specify data requirements, model architectures, evaluation metrics, and integration points. "
            "Design with MLOps best practices: versioning, monitoring, and iterative improvement."
        ),
        expected_output=(
            "A markdown file 'ml_systems_design.md' with:\n"
            "- ML system architecture and components\n"
            "- Recommendation engine design (collaborative filtering, content-based, hybrid)\n"
            "- Adaptive learning model specifications\n"
            "- Knowledge tracing approach (BKT, DKT, or other)\n"
            "- Feature engineering and data requirements\n"
            "- Model evaluation metrics and success criteria\n"
            "- MLOps pipeline (training, deployment, monitoring)\n"
            "- MVP simplifications vs. future enhancements"
        ),
        agent=ml_engineer,
        output_file=str(artifacts_dir / "ml_systems_design.md"),
        context=[task_design_data_infrastructure]
    )

    task_design_llm_integration = Task(
        description=(
            "Design the LLM integration strategy for intelligent tutoring and personalized learning experiences. "
            "Plan how to use GPT-4, Claude, or other LLMs for:\n\n"
            "- AI tutor for answering learner questions\n"
            "- Personalized explanations and examples\n"
            "- Code review and debugging assistance\n"
            "- Socratic dialogue for deeper understanding\n"
            "- Content generation and adaptation\n\n"
            "Design prompt engineering strategies, RAG systems for course content, and cost management. "
            "Ensure pedagogically sound AI interactions that guide learning rather than just giving answers."
        ),
        expected_output=(
            "A markdown file 'llm_integration_design.md' with:\n"
            "- LLM use cases and integration points\n"
            "- Prompt engineering strategies and templates\n"
            "- RAG system design (vector DB, embedding strategy, retrieval)\n"
            "- Conversation flow and dialogue management\n"
            "- Guardrails and safety measures (prevent hallucinations, ensure pedagogical alignment)\n"
            "- Cost management and optimization strategies\n"
            "- Evaluation framework for LLM responses\n"
            "- MVP implementation plan (which features first)"
        ),
        agent=llm_engineer,
        output_file=str(artifacts_dir / "llm_integration_design.md"),
        context=[task_create_system_architecture]
    )

    task_create_mvp_plan = Task(
        description=(
            "Synthesize all technical designs into a concrete MVP implementation plan. Based on the UX, "
            "architecture, and specialized system designs, create a detailed development plan:\n\n"
            "- Prioritized feature list for MVP\n"
            "- Technical specifications for each feature\n"
            "- Development phases and milestones\n"
            "- Technology choices and setup instructions\n"
            "- API contracts and integration points\n"
            "- Testing strategy\n"
            "- Deployment checklist\n\n"
            "This should be detailed enough for a developer to start building immediately."
        ),
        expected_output=(
            "A markdown file 'mvp_implementation_plan.md' with:\n"
            "- Prioritized MVP feature list with acceptance criteria\n"
            "- Development phases (e.g., Week 1-2: Auth + DB, Week 3-4: Content delivery, etc.)\n"
            "- Detailed technical specs for each feature\n"
            "- Tech stack setup guide\n"
            "- API endpoint specifications\n"
            "- Database migration plan\n"
            "- Testing and QA strategy\n"
            "- Deployment and launch checklist\n"
            "- Known limitations and future enhancements"
        ),
        agent=fullstack_dev,
        output_file=str(artifacts_dir / "mvp_implementation_plan.md"),
        context=[
            task_design_ux,
            task_create_system_architecture,
            task_design_data_infrastructure,
            task_design_ml_systems,
            task_design_llm_integration
        ]
    )

    return [
        task_design_ux,
        task_create_system_architecture,
        task_design_data_infrastructure,
        task_design_ml_systems,
        task_design_llm_integration,
        task_create_mvp_plan
    ]
