"""Tasks for the QA Crew (Phase 4: Testing & Refinement)."""

from crewai import Task
from core.config import Config


def get_qa_tasks(qa_researcher) -> list:
    """
    Get tasks for Phase 4: Testing & Refinement.

    Returns:
        List of CrewAI Task objects
    """
    artifacts_dir = Config.ARTIFACTS_DIR

    task_comprehensive_review = Task(
        description=(
            "Conduct a comprehensive review and evaluation of all artifacts produced so far. "
            "Assess the complete AI Mastery Platform design across multiple dimensions:\n\n"
            "**Educational Effectiveness:**\n"
            "- Do learning objectives align with curriculum content?\n"
            "- Is the curriculum pedagogically sound and evidence-based?\n"
            "- Will learners actually achieve mastery, or just surface knowledge?\n"
            "- Are assessments aligned with learning outcomes?\n\n"
            "**Technical Quality:**\n"
            "- Is the system architecture robust and scalable?\n"
            "- Are the technical designs feasible and well-specified?\n"
            "- Are there gaps or inconsistencies in technical planning?\n\n"
            "**User Experience:**\n"
            "- Is the UX intuitive and learner-friendly?\n"
            "- Does the platform remove friction from the learning process?\n"
            "- Are engagement systems well-designed and non-manipulative?\n\n"
            "**Coherence:**\n"
            "- Do all components work together harmoniously?\n"
            "- Are there conflicts or misalignments between divisions' work?\n\n"
            "Be thorough, critical, and constructive. Identify strengths, weaknesses, gaps, and risks."
        ),
        expected_output=(
            "A markdown file 'qa_comprehensive_review.md' with:\n"
            "- Executive summary of overall assessment\n"
            "- Dimension-by-dimension evaluation (educational, technical, UX, coherence)\n"
            "- Strengths and what's working well\n"
            "- Critical gaps and weaknesses\n"
            "- Specific issues identified with references to source artifacts\n"
            "- Risk assessment (what could go wrong?)\n"
            "- Comparison to industry best practices and successful learning platforms"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "qa_comprehensive_review.md")
    )

    task_create_refinement_backlog = Task(
        description=(
            "Based on the comprehensive review, create a prioritized backlog of refinements and improvements. "
            "Organize recommendations into:\n\n"
            "- **Critical fixes**: Issues that must be addressed before MVP launch\n"
            "- **High-priority improvements**: Important enhancements that significantly improve quality\n"
            "- **Medium-priority enhancements**: Valuable additions for post-MVP iterations\n"
            "- **Long-term considerations**: Ideas for future phases\n\n"
            "For each item, provide:\n"
            "- Clear description of the issue or opportunity\n"
            "- Rationale and impact assessment\n"
            "- Suggested solution or approach\n"
            "- Estimated effort (small/medium/large)\n"
            "- Affected artifacts or systems\n\n"
            "Prioritize ruthlessly: what truly matters for learner success?"
        ),
        expected_output=(
            "A markdown file 'refinement_backlog.md' with:\n"
            "- Prioritized list of improvements (Critical → High → Medium → Long-term)\n"
            "- Each item with: description, rationale, impact, solution, effort estimate\n"
            "- Quick wins that deliver high value with low effort\n"
            "- Recommendations for immediate next steps\n"
            "- Metrics to track improvement effectiveness"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "refinement_backlog.md"),
        context=[task_comprehensive_review]
    )

    task_validation_framework = Task(
        description=(
            "Design a framework for validating and measuring the platform's effectiveness once built. "
            "Create plans for:\n\n"
            "- Learning outcome measurement (how to assess if learners achieve mastery)\n"
            "- User research protocols (interviews, usability testing, think-alouds)\n"
            "- Analytics and metrics to track (engagement, completion, skill growth)\n"
            "- A/B testing framework for iterative improvement\n"
            "- Feedback collection mechanisms\n\n"
            "Design both formative evaluation (during development) and summative evaluation (post-launch). "
            "Specify what data to collect and how to interpret it."
        ),
        expected_output=(
            "A markdown file 'validation_framework.md' with:\n"
            "- Learning outcome assessment strategy\n"
            "- User research plan and protocols\n"
            "- Key metrics and KPIs to track\n"
            "- Analytics instrumentation requirements\n"
            "- A/B testing framework and hypothesis templates\n"
            "- Feedback loops and continuous improvement process\n"
            "- Evaluation timeline and milestones"
        ),
        agent=qa_researcher,
        output_file=str(artifacts_dir / "validation_framework.md"),
        context=[task_comprehensive_review, task_create_refinement_backlog]
    )

    return [
        task_comprehensive_review,
        task_create_refinement_backlog,
        task_validation_framework
    ]
