"""Tasks for the Curriculum Crew (Phase 2: Curriculum Construction)."""

from crewai import Task
from core.config import Config


def get_curriculum_tasks(
    curriculum_architect,
    ai_sme,
    instructional_designer,
    cognitive_scientist,
    behavior_designer
) -> list:
    """
    Get tasks for Phase 2: Curriculum Construction.

    Returns:
        List of CrewAI Task objects
    """
    artifacts_dir = Config.ARTIFACTS_DIR

    task_create_curriculum_scaffold = Task(
        description=(
            "Design a comprehensive curriculum scaffold for AI mastery. Based on the learning objectives, "
            "create a structured learning path with modules, topics, and progression.\n\n"
            "Structure the curriculum with:\n"
            "- Clear module organization (e.g., Foundations → Deep Learning → NLP → LLMs → Advanced Topics)\n"
            "- Topic sequencing with explicit prerequisites\n"
            "- Estimated time commitments per module\n"
            "- Learning outcomes for each module\n"
            "- Skill progression from beginner to advanced\n\n"
            "Ensure logical flow: each topic builds on previous knowledge. Include both theoretical concepts "
            "and hands-on practical skills."
        ),
        expected_output=(
            "A markdown file 'curriculum_scaffold.md' with:\n"
            "- Overview of curriculum structure\n"
            "- Detailed module breakdown with topics and subtopics\n"
            "- Dependency graph showing prerequisites\n"
            "- Time estimates for each module\n"
            "- Learning outcomes mapped to original objectives\n"
            "- Suggested learning pathways (e.g., practitioner track vs. researcher track)"
        ),
        agent=curriculum_architect,
        output_file=str(artifacts_dir / "curriculum_scaffold.md")
    )

    task_validate_technical_depth = Task(
        description=(
            "Review the curriculum scaffold for technical accuracy, depth, and industry relevance. "
            "As an AI subject matter expert, ensure that:\n\n"
            "- All essential AI/ML concepts are covered\n"
            "- Technical depth is appropriate for mastery (not just surface-level)\n"
            "- Content reflects current best practices and state-of-the-art techniques\n"
            "- Balance between theory and practical application is appropriate\n"
            "- Common pitfalls and misconceptions are addressed\n\n"
            "Identify gaps, recommend additions, and suggest depth adjustments. Validate that completing "
            "this curriculum would truly prepare someone for professional AI/ML work."
        ),
        expected_output=(
            "A markdown file 'technical_validation.md' with:\n"
            "- Assessment of technical coverage and depth\n"
            "- Gaps or missing topics identified\n"
            "- Recommendations for additions or modifications\n"
            "- Suggested resources and references for each module\n"
            "- Industry alignment assessment (what real ML engineers need to know)"
        ),
        agent=ai_sme,
        output_file=str(artifacts_dir / "technical_validation.md"),
        context=[task_create_curriculum_scaffold]
    )

    task_apply_learning_science = Task(
        description=(
            "Apply cognitive science principles to optimize the curriculum for learning effectiveness. "
            "Review the curriculum structure and recommend enhancements based on:\n\n"
            "- Cognitive load management (chunking, progressive disclosure)\n"
            "- Spaced repetition and interleaving\n"
            "- Retrieval practice and testing effects\n"
            "- Transfer learning and far transfer\n"
            "- Desirable difficulties and productive struggle\n\n"
            "Ensure the curriculum aligns with how the brain actually learns complex technical material. "
            "Recommend specific strategies for memory consolidation and skill acquisition."
        ),
        expected_output=(
            "A markdown file 'learning_science_overlay.md' with:\n"
            "- Analysis of curriculum through cognitive science lens\n"
            "- Specific recommendations for each module (spacing, practice schedules, etc.)\n"
            "- Suggestions for retrieval practice and formative assessment\n"
            "- Strategies to prevent cognitive overload\n"
            "- Recommendations for transfer activities and application exercises"
        ),
        agent=cognitive_scientist,
        output_file=str(artifacts_dir / "learning_science_overlay.md"),
        context=[task_create_curriculum_scaffold, task_validate_technical_depth]
    )

    task_design_instructional_content = Task(
        description=(
            "Transform the validated curriculum scaffold into detailed instructional content outlines. "
            "For each module, design:\n\n"
            "- Lesson structures and learning activities\n"
            "- Mix of content types (readings, videos, interactive exercises, projects)\n"
            "- Formative and summative assessments\n"
            "- Hands-on coding projects and case studies\n"
            "- Scaffolded practice exercises (guided → semi-guided → independent)\n\n"
            "Create engaging, active learning experiences that go beyond passive content consumption. "
            "Include Socratic questioning, problem-solving activities, and real-world applications."
        ),
        expected_output=(
            "A markdown file 'instructional_content_outline.md' with:\n"
            "- Detailed lesson plans for key modules\n"
            "- Learning activity types and formats\n"
            "- Assessment strategies (quizzes, projects, peer review)\n"
            "- Example project descriptions and rubrics\n"
            "- Interactive exercise concepts (e.g., 'Build a transformer from scratch' walkthrough)"
        ),
        agent=instructional_designer,
        output_file=str(artifacts_dir / "instructional_content_outline.md"),
        context=[task_create_curriculum_scaffold, task_apply_learning_science]
    )

    task_design_engagement_systems = Task(
        description=(
            "Design behavior systems and engagement mechanics to support long-term learning commitment. "
            "Create systems that:\n\n"
            "- Foster daily learning habits\n"
            "- Provide meaningful progress feedback\n"
            "- Balance intrinsic and extrinsic motivation\n"
            "- Create 'tiny habits' that compound over time\n"
            "- Maintain engagement through inevitable difficulty plateaus\n\n"
            "Design feedback loops, progress visualization, streak mechanics, milestone celebrations, "
            "and other behavioral nudges. Ensure systems support mastery orientation, not just completion."
        ),
        expected_output=(
            "A markdown file 'engagement_systems.md' with:\n"
            "- Habit formation strategies and prompts\n"
            "- Progress tracking and visualization designs\n"
            "- Motivational triggers and feedback loops\n"
            "- Streak and consistency mechanics\n"
            "- Milestone and achievement system\n"
            "- Strategies for maintaining motivation during difficult modules"
        ),
        agent=behavior_designer,
        output_file=str(artifacts_dir / "engagement_systems.md"),
        context=[task_create_curriculum_scaffold, task_design_instructional_content]
    )

    return [
        task_create_curriculum_scaffold,
        task_validate_technical_depth,
        task_apply_learning_science,
        task_design_instructional_content,
        task_design_engagement_systems
    ]
