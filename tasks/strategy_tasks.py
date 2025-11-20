"""Tasks for the Strategy Crew (Phase 1: Vision & Requirements)."""

from pathlib import Path
from crewai import Task
from core.config import Config
from core.user_profile import format_profile_for_agents


def get_strategy_tasks(chief_of_staff, product_manager) -> list:
    """
    Get tasks for Phase 1: Vision & Requirements.

    Returns:
        List of CrewAI Task objects
    """
    artifacts_dir = Config.ARTIFACTS_DIR

    # Get user profile context
    user_profile = Config.get_user_profile()
    profile_context = format_profile_for_agents(user_profile) if user_profile else "\nNo user profile provided. Use generic AI mastery goals.\n"

    task_define_objectives = Task(
        description=(
            f"{profile_context}\n\n"
            "Define clear, PERSONALIZED learning objectives for this specific user's AI Mastery journey. "
            "Work with the user's stated goals, current level, target role, and constraints to create "
            "a comprehensive list of what they should know and be able to do after completing the learning journey.\n\n"
            "Structure objectives using Bloom's taxonomy (remember, understand, apply, analyze, evaluate, create). "
            "Tailor the depth and focus based on:\n"
            "- Their target role and industry\n"
            "- Current Python/AI skill level\n"
            "- Specific AI focus area of interest\n"
            "- Time available and learning constraints\n\n"
            "Consider areas like:\n"
            "- Core AI/ML fundamentals (adjust depth based on current level)\n"
            "- Deep learning and neural networks\n"
            "- NLP and transformer architectures\n"
            "- LLM fine-tuning and prompt engineering\n"
            "- AI system design and deployment\n"
            "- Ethics and responsible AI\n"
            "- Industry-specific applications relevant to their field\n\n"
            "Output: A detailed markdown document with categorized, personalized learning objectives."
        ),
        expected_output=(
            "A markdown file 'learning_objectives.md' with:\n"
            "- Executive summary of the learning vision\n"
            "- Categorized learning objectives by domain (Fundamentals, Deep Learning, NLP, LLMs, etc.)\n"
            "- Each objective mapped to Bloom's taxonomy level\n"
            "- Success criteria for each objective"
        ),
        agent=chief_of_staff,
        output_file=str(artifacts_dir / "learning_objectives.md")
    )

    task_create_prd = Task(
        description=(
            f"{profile_context}\n\n"
            "Create a comprehensive, PERSONALIZED Product Requirements Document (PRD) for this user's "
            "AI Mastery Platform MVP. Based on the learning objectives AND the user's specific constraints, "
            "define the platform's core features, user stories, and technical requirements.\n\n"
            "The PRD should cover:\n"
            "- Product vision and goals (aligned with user's target role and industry)\n"
            "- Target user persona (THIS specific learner - use their actual profile)\n"
            "- Core features for MVP tailored to:\n"
            "  * Their available time and schedule (weekends, daily hours)\n"
            "  * Their hardware constraints (local vs cloud)\n"
            "  * Their budget limitations\n"
            "  * Their focus area preference\n"
            "  * Their portfolio goals (public vs private)\n"
            "- User stories and acceptance criteria\n"
            "- Success metrics and KPIs relevant to their goals\n"
            "- Technical constraints based on their hardware/budget\n"
            "- Out of scope (what we're NOT building in MVP)\n\n"
            "Think like a PM: What's the minimum viable product that delivers real value for THIS specific user "
            "and enables progress towards THEIR AI mastery goals? Avoid feature creep."
        ),
        expected_output=(
            "A markdown file 'prd.md' with:\n"
            "- Product vision statement\n"
            "- User persona and journey\n"
            "- Prioritized feature list (Must-have, Should-have, Nice-to-have)\n"
            "- Detailed user stories with acceptance criteria\n"
            "- Success metrics (engagement, completion rates, skill mastery)\n"
            "- Technical requirements and constraints\n"
            "- MVP scope and timeline estimate"
        ),
        agent=product_manager,
        output_file=str(artifacts_dir / "prd.md"),
        context=[task_define_objectives]
    )

    task_create_roadmap = Task(
        description=(
            f"{profile_context}\n\n"
            "Create a high-level, REALISTIC product roadmap and phase plan for building this user's "
            "personalized AI Mastery Platform. Based on the PRD and user's time/resource constraints, "
            "sequence the development effort into logical phases.\n\n"
            "Consider the user's:\n"
            "- Available learning time ({user_profile.get('time_available', 'not specified') if user_profile else 'not specified'})\n"
            "- Budget constraints ({user_profile.get('budget', 'not specified') if user_profile else 'not specified'})\n"
            "- Hardware limitations\n"
            "- Company alignment goals\n\n"
            "Suggest phases like:\n"
            "- Phase 1 (MVP): Core content delivery and progress tracking (adapt timeline to user's availability)\n"
            "- Phase 2 (Enhanced): Personalization and adaptive learning\n"
            "- Phase 3 (Advanced): LLM-powered tutoring (if budget allows)\n"
            "- Phase 4 (Scale): Analytics, optimization, and content expansion\n\n"
            "For the MVP phase, provide a detailed breakdown of deliverables and milestones that are "
            "REALISTIC given the user's time constraints. Don't suggest a 6-month plan if they only have "
            "1 hour per day."
        ),
        expected_output=(
            "A markdown file 'roadmap.md' with:\n"
            "- Multi-phase product roadmap\n"
            "- Detailed MVP milestone breakdown\n"
            "- Dependencies between phases\n"
            "- Risk assessment and mitigation strategies\n"
            "- Resource requirements (APIs, infrastructure, etc.)"
        ),
        agent=chief_of_staff,
        output_file=str(artifacts_dir / "roadmap.md"),
        context=[task_define_objectives, task_create_prd]
    )

    return [task_define_objectives, task_create_prd, task_create_roadmap]
