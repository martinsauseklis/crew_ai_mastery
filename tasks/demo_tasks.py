"""Simplified tasks for demo mode - all 17 tasks with reduced scope."""

from pathlib import Path
from crewai import Task
from demo_config import DemoConfig
from demo_profile import format_demo_profile_for_agents
from core.config import Config


# ============================================================================
# PHASE 1: STRATEGY TASKS (3 tasks)
# ============================================================================

def get_demo_strategy_tasks(chief_of_staff, product_manager) -> list:
    """Get simplified tasks for Phase 1: Vision & Requirements (DEMO)."""
    artifacts_dir = DemoConfig.get_demo_artifacts_dir()

    # Get user profile context
    user_profile = Config.get_user_profile()
    profile_context = format_demo_profile_for_agents(user_profile) if user_profile else "\nNo user profile provided.\n"

    task_define_objectives = Task(
        description=(
            f"{profile_context}\n\n"
            "Define 5-7 key learning objectives for this user's AI mastery journey. "
            "Focus on their target role and experience level. Structure using Bloom's taxonomy.\n\n"
            "Cover: Core AI/ML fundamentals, Deep Learning, NLP/LLMs, and practical deployment.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Show taxonomy mapping and success criteria "
            "for a few key objectives as examples."
        ),
        expected_output=(
            "A concise markdown file 'learning_objectives.md' with:\n"
            "- Executive summary\n"
            "- 5-7 categorized learning objectives with Bloom's taxonomy levels\n"
            "- Success criteria for each\n"
            "(Target: ~300-400 words)"
        ),
        agent=chief_of_staff,
        output_file=str(artifacts_dir / "learning_objectives.md")
    )

    task_create_prd = Task(
        description=(
            f"{profile_context}\n\n"
            "Create a concise PRD for the AI Mastery Platform MVP. Based on learning objectives "
            "and user constraints, define core features and requirements.\n\n"
            "Include: Product vision, target persona (this user), 3-5 must-have MVP features, "
            "2-3 key user stories, success metrics, and technical constraints.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Focus on the essential MVP scope."
        ),
        expected_output=(
            "A concise markdown file 'prd.md' with:\n"
            "- Product vision\n"
            "- User persona\n"
            "- Prioritized features (3-5 must-haves)\n"
            "- Key user stories\n"
            "- Success metrics\n"
            "(Target: ~400-500 words)"
        ),
        agent=product_manager,
        output_file=str(artifacts_dir / "prd.md"),
        context=[task_define_objectives]
    )

    task_create_roadmap = Task(
        description=(
            f"{profile_context}\n\n"
            "Create a high-level product roadmap with 3-4 phases. Focus on MVP phase details.\n\n"
            "Consider user's time constraints and budget. Suggest realistic phasing:\n"
            "- Phase 1 (MVP): Core features\n"
            "- Phase 2: Personalization\n"
            "- Phase 3: Advanced features\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Focus on MVP breakdown."
        ),
        expected_output=(
            "A concise markdown file 'roadmap.md' with:\n"
            "- Multi-phase roadmap overview\n"
            "- Detailed MVP milestones\n"
            "- Key dependencies\n"
            "(Target: ~300-400 words)"
        ),
        agent=chief_of_staff,
        output_file=str(artifacts_dir / "roadmap.md"),
        context=[task_define_objectives, task_create_prd]
    )

    return [task_define_objectives, task_create_prd, task_create_roadmap]


# ============================================================================
# PHASE 2: CURRICULUM TASKS (5 tasks)
# ============================================================================

def get_demo_curriculum_tasks(
    curriculum_architect,
    ai_sme,
    instructional_designer,
    cognitive_scientist,
    behavior_designer
) -> list:
    """Get simplified tasks for Phase 2: Curriculum Construction (DEMO)."""
    artifacts_dir = DemoConfig.get_demo_artifacts_dir()

    task_create_curriculum_scaffold = Task(
        description=(
            "Design a curriculum scaffold with 4-6 modules for AI mastery. "
            "Create a structured learning path with clear progression.\n\n"
            "Include module organization, topic sequencing, time estimates, and learning outcomes.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Show structure with 4-6 modules as examples."
        ),
        expected_output=(
            "A concise markdown file 'curriculum_scaffold.md' with:\n"
            "- Curriculum structure overview\n"
            "- 4-6 modules with topics\n"
            "- Prerequisites and time estimates\n"
            "(Target: ~400-500 words)"
        ),
        agent=curriculum_architect,
        output_file=str(artifacts_dir / "curriculum_scaffold.md")
    )

    task_validate_technical_depth = Task(
        description=(
            "Review the curriculum scaffold for technical accuracy and depth. "
            "Ensure essential AI/ML concepts are covered with appropriate depth.\n\n"
            "Identify 2-3 key gaps or recommendations for improvement.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Focus on main insights."
        ),
        expected_output=(
            "A concise markdown file 'technical_validation.md' with:\n"
            "- Technical coverage assessment\n"
            "- 2-3 key gaps or recommendations\n"
            "- Suggested resources\n"
            "(Target: ~300-400 words)"
        ),
        agent=ai_sme,
        output_file=str(artifacts_dir / "technical_validation.md"),
        context=[task_create_curriculum_scaffold]
    )

    task_apply_learning_science = Task(
        description=(
            "Apply cognitive science principles to optimize the curriculum. "
            "Recommend enhancements based on cognitive load, spaced repetition, and retrieval practice.\n\n"
            "Provide 3-5 specific recommendations with examples.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Focus on key principles."
        ),
        expected_output=(
            "A concise markdown file 'learning_science_overlay.md' with:\n"
            "- Key cognitive science principles applied\n"
            "- 3-5 specific recommendations\n"
            "- Example implementation\n"
            "(Target: ~300-400 words)"
        ),
        agent=cognitive_scientist,
        output_file=str(artifacts_dir / "learning_science_overlay.md"),
        context=[task_create_curriculum_scaffold, task_validate_technical_depth]
    )

    task_create_instructional_content = Task(
        description=(
            "Create an instructional content outline for 2-3 sample modules. "
            "Include lesson structure, activities, and assessments.\n\n"
            "Show concrete examples of how content will be delivered.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Focus on 2-3 module examples."
        ),
        expected_output=(
            "A concise markdown file 'instructional_content_outline.md' with:\n"
            "- Content outline for 2-3 sample modules\n"
            "- Lesson structure and activities\n"
            "- Assessment approach\n"
            "(Target: ~400-500 words)"
        ),
        agent=instructional_designer,
        output_file=str(artifacts_dir / "instructional_content_outline.md"),
        context=[task_create_curriculum_scaffold, task_apply_learning_science]
    )

    task_design_engagement_systems = Task(
        description=(
            "Design engagement and habit formation systems for the platform. "
            "Create mechanisms for motivation, accountability, and sustained learning.\n\n"
            "Include 3-5 specific engagement features with examples.\n\n"
            "DEMO MODE: Keep output concise (300-400 words)."
        ),
        expected_output=(
            "A concise markdown file 'engagement_systems.md' with:\n"
            "- 3-5 engagement mechanisms\n"
            "- Habit formation strategies\n"
            "- Motivation and accountability features\n"
            "(Target: ~300-400 words)"
        ),
        agent=behavior_designer,
        output_file=str(artifacts_dir / "engagement_systems.md"),
        context=[task_create_curriculum_scaffold, task_create_instructional_content]
    )

    return [
        task_create_curriculum_scaffold,
        task_validate_technical_depth,
        task_apply_learning_science,
        task_create_instructional_content,
        task_design_engagement_systems
    ]


# ============================================================================
# PHASE 3: PLATFORM TASKS (6 tasks)
# ============================================================================

def get_demo_platform_tasks(
    ux_designer,
    fullstack_developer,
    backend_engineer,
    ml_engineer,
    llm_engineer
) -> list:
    """Get simplified tasks for Phase 3: Product & Platform Build (DEMO)."""
    artifacts_dir = DemoConfig.get_demo_artifacts_dir()

    task_design_ux = Task(
        description=(
            "Design the UX/UI for the AI Mastery Platform. Create information architecture, "
            "key user flows, and design system foundations.\n\n"
            "Focus on: onboarding, lesson consumption, progress tracking.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Show 2-3 key flows."
        ),
        expected_output=(
            "A concise markdown file 'ux_design.md' with:\n"
            "- Information architecture\n"
            "- 2-3 key user flows\n"
            "- Design system foundations\n"
            "(Target: ~400-500 words)"
        ),
        agent=ux_designer,
        output_file=str(artifacts_dir / "ux_design.md")
    )

    task_create_system_architecture = Task(
        description=(
            "Design the technical architecture for the platform. Cover frontend, backend, "
            "database, and deployment.\n\n"
            "Choose pragmatic technologies for MVP. Document key decisions.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Focus on core architecture."
        ),
        expected_output=(
            "A concise markdown file 'system_architecture.md' with:\n"
            "- Architecture overview\n"
            "- Technology stack\n"
            "- Key components and data flow\n"
            "(Target: ~400-500 words)"
        ),
        agent=fullstack_developer,
        output_file=str(artifacts_dir / "system_architecture.md"),
        context=[task_design_ux]
    )

    task_design_data_infrastructure = Task(
        description=(
            "Design the data infrastructure for learning analytics and progress tracking. "
            "Create database schema and data pipeline design.\n\n"
            "Include key entities: users, content, progress, analytics.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Show core schema."
        ),
        expected_output=(
            "A concise markdown file 'data_infrastructure.md' with:\n"
            "- Database schema for core entities\n"
            "- Data pipeline design\n"
            "- Analytics approach\n"
            "(Target: ~300-400 words)"
        ),
        agent=backend_engineer,
        output_file=str(artifacts_dir / "data_infrastructure.md"),
        context=[task_create_system_architecture]
    )

    task_design_ml_systems = Task(
        description=(
            "Design ML-powered personalization systems. Create adaptive learning paths "
            "and recommendation engine design.\n\n"
            "Include: user modeling, content recommendations, difficulty adaptation.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Focus on core ML features."
        ),
        expected_output=(
            "A concise markdown file 'ml_systems_design.md' with:\n"
            "- Personalization approach\n"
            "- ML models and features\n"
            "- Implementation strategy\n"
            "(Target: ~300-400 words)"
        ),
        agent=ml_engineer,
        output_file=str(artifacts_dir / "ml_systems_design.md"),
        context=[task_create_system_architecture, task_design_data_infrastructure]
    )

    task_design_llm_integration = Task(
        description=(
            "Design LLM integration for AI tutoring and interactive help. "
            "Create prompting strategies and conversation design.\n\n"
            "Include: tutor persona, prompt templates, context management.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Show key integration points."
        ),
        expected_output=(
            "A concise markdown file 'llm_integration_design.md' with:\n"
            "- LLM integration approach\n"
            "- Tutor persona and prompts\n"
            "- Context management strategy\n"
            "(Target: ~300-400 words)"
        ),
        agent=llm_engineer,
        output_file=str(artifacts_dir / "llm_integration_design.md"),
        context=[task_create_system_architecture]
    )

    task_create_mvp_plan = Task(
        description=(
            "Create a detailed MVP implementation plan. Sequence development into sprints "
            "with clear deliverables.\n\n"
            "Include: feature prioritization, 3-4 sprint breakdown, technical milestones.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Focus on first 3-4 sprints."
        ),
        expected_output=(
            "A concise markdown file 'mvp_implementation_plan.md' with:\n"
            "- MVP scope and priorities\n"
            "- Sprint breakdown (3-4 sprints)\n"
            "- Technical milestones\n"
            "(Target: ~400-500 words)"
        ),
        agent=fullstack_developer,
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


# ============================================================================
# PHASE 4: QA TASKS (3 tasks)
# ============================================================================

def get_demo_qa_tasks(qa_researcher) -> list:
    """Get simplified tasks for Phase 4: Testing & Refinement (DEMO)."""
    artifacts_dir = DemoConfig.get_demo_artifacts_dir()

    task_comprehensive_review = Task(
        description=(
            "Conduct a comprehensive review of all deliverables from Phases 1-3. "
            "Evaluate alignment, completeness, and quality.\n\n"
            "Assess: strategic alignment, curriculum quality, technical feasibility, UX effectiveness.\n\n"
            "DEMO MODE: Keep output concise (400-500 words). Provide key insights and ratings."
        ),
        expected_output=(
            "A concise markdown file 'qa_comprehensive_review.md' with:\n"
            "- Multi-dimensional evaluation\n"
            "- Quality ratings by category\n"
            "- Key findings and concerns\n"
            "(Target: ~400-500 words)"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "qa_comprehensive_review.md")
    )

    task_create_refinement_backlog = Task(
        description=(
            "Create a prioritized refinement backlog based on the comprehensive review. "
            "Identify top improvements needed.\n\n"
            "Categorize by: Critical fixes, High-value improvements, Nice-to-haves.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Focus on top 5-7 items."
        ),
        expected_output=(
            "A concise markdown file 'refinement_backlog.md' with:\n"
            "- Prioritized improvement list (5-7 top items)\n"
            "- Categorization by priority\n"
            "- Recommended action for each\n"
            "(Target: ~300-400 words)"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "refinement_backlog.md"),
        context=[task_comprehensive_review]
    )

    task_create_validation_framework = Task(
        description=(
            "Design a validation framework for measuring platform success. "
            "Create metrics, KPIs, and evaluation protocols.\n\n"
            "Include: learning outcomes metrics, engagement metrics, business metrics.\n\n"
            "DEMO MODE: Keep output concise (300-400 words). Show key metrics and measurement approach."
        ),
        expected_output=(
            "A concise markdown file 'validation_framework.md' with:\n"
            "- Key success metrics by category\n"
            "- Measurement protocols\n"
            "- Evaluation timeline\n"
            "(Target: ~300-400 words)"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "validation_framework.md"),
        context=[task_comprehensive_review]
    )

    return [
        task_comprehensive_review,
        task_create_refinement_backlog,
        task_create_validation_framework
    ]
