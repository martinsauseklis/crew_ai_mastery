"""Validation tasks for testing the AI Mastery Platform"""

from pathlib import Path
from crewai import Task
from demo_config import DemoConfig


def get_validator_tasks(
    backend_validator,
    frontend_validator,
    integration_validator,
    data_validator,
    debug_assistant
) -> list:
    """Get validation tasks for testing the platform"""

    platform_dir = DemoConfig.get_demo_artifacts_dir() / "platform_code"
    backend_dir = platform_dir / "backend"
    frontend_dir = platform_dir / "frontend"

    task_validate_backend = Task(
        description=(
            f"Validate the backend implementation in {backend_dir}\n\n"
            "Test the following:\n"
            "1. **Database Models** (models.py):\n"
            "   - Check all relationships are bidirectional\n"
            "   - Verify foreign keys exist and are correct\n"
            "   - Test that User, Course, Module, Lesson, DailyTask, TaskCompletion, Progress models are complete\n"
            "   - Validate JSON fields are properly configured\n\n"
            "2. **API Endpoints** (app.py):\n"
            "   - Test GET /api/courses returns courses\n"
            "   - Test GET /api/progress?user_id=X works\n"
            "   - Test POST /api/auth/register creates user\n"
            "   - Test POST /api/auth/login returns token\n"
            "   - Check error handling for invalid inputs\n\n"
            "3. **Seed Data** (seed_data.py):\n"
            "   - Verify it creates demo user, Module 1, Week 1, Day 1 lesson\n"
            "   - Check it creates 5 Day 1 tasks\n"
            "   - Validate foreign key references\n"
            "   - Test idempotency (can run multiple times)\n\n"
            "4. **Configuration**:\n"
            "   - Validate database.py settings\n"
            "   - Check config.py environment variables\n"
            "   - Test auth.py password hashing\n\n"
            "**Testing Approach:**\n"
            "- Read each file and analyze the code\n"
            "- Identify potential runtime errors, logic bugs, missing imports\n"
            "- Check for SQLAlchemy common mistakes\n"
            "- Verify FastAPI route definitions\n\n"
            "**Output:** Create a detailed validation report listing:\n"
            "- ✅ What works correctly\n"
            "- ❌ What is broken or missing\n"
            "- 🔧 Specific code fixes for each issue (with before/after examples)\n"
        ),
        expected_output=(
            "A comprehensive backend validation report including:\n"
            "- Model validation results (pass/fail for each model)\n"
            "- API endpoint test results\n"
            "- Seed data validation results\n"
            "- List of bugs found with severity (Critical, Major, Minor)\n"
            "- Code fixes for each bug (exact Python code to replace)\n"
            "(Target: 800-1000 words with code examples)"
        ),
        agent=backend_validator,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "backend_validation_report.md")
    )

    task_validate_frontend = Task(
        description=(
            f"Validate the frontend implementation in {frontend_dir}\n\n"
            "Test the following:\n"
            "1. **React Components**:\n"
            "   - pages/index.tsx - Check Link usage (Next.js 13+ syntax)\n"
            "   - pages/login.tsx - Verify form handling and router usage\n"
            "   - pages/dashboard.tsx - Check data display and navigation\n"
            "   - components/Navigation.tsx - Validate all links\n"
            "   - components/CourseCard.tsx - Check props and TypeScript types\n"
            "   - components/ProgressBar.tsx - Validate progress display\n\n"
            "2. **Configuration Files**:\n"
            "   - package.json - Verify dependencies are compatible\n"
            "   - next.config.js - Check Next.js settings\n"
            "   - tailwind.config.js - Validate Tailwind setup\n"
            "   - tsconfig.json - Check TypeScript configuration\n"
            "   - pages/_app.tsx - Verify global styles import\n\n"
            "3. **Common Issues**:\n"
            "   - Link with nested <a> tags (should be fixed)\n"
            "   - Missing imports\n"
            "   - TypeScript errors\n"
            "   - Routing issues\n"
            "   - CSS class name errors\n\n"
            "4. **User Flows**:\n"
            "   - Can user navigate from home → login → dashboard?\n"
            "   - Are all pages accessible?\n"
            "   - Does navigation component work on all pages?\n\n"
            "**Output:** Create a validation report with:\n"
            "- Component-by-component analysis\n"
            "- List of any remaining errors\n"
            "- Code fixes (exact TSX code)\n"
        ),
        expected_output=(
            "A frontend validation report including:\n"
            "- Component validation results\n"
            "- Configuration file checks\n"
            "- List of bugs/warnings found\n"
            "- Code fixes with before/after examples\n"
            "- User flow test results\n"
            "(Target: 600-800 words with code examples)"
        ),
        agent=frontend_validator,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "frontend_validation_report.md"),
        context=[task_validate_backend]  # Can reference backend findings
    )

    task_validate_integration = Task(
        description=(
            "Test end-to-end user flows to ensure frontend, backend, and database work together.\n\n"
            "**Test Scenarios:**\n\n"
            "1. **User Registration Flow:**\n"
            "   - Frontend: POST to /api/auth/register from login page\n"
            "   - Backend: Creates user in database\n"
            "   - Database: User record exists with hashed password\n"
            "   - Verify: Check models.py User model has all required fields\n\n"
            "2. **Course Enrollment Flow:**\n"
            "   - User logs in → sees dashboard\n"
            "   - Frontend GET /api/courses → displays Module 1\n"
            "   - User clicks Module 1 → GET /api/courses/{id}\n"
            "   - Shows Week 1, Day 1 lesson\n"
            "   - Verify: Progress model tracks current lesson\n\n"
            "3. **Lesson Completion Flow:**\n"
            "   - User starts Day 1\n"
            "   - Frontend shows 5 tasks\n"
            "   - User completes task → POST /api/tasks/{id}/complete\n"
            "   - Backend: Updates TaskCompletion table\n"
            "   - Updates progress percentage and streak\n"
            "   - Verify: Foreign keys work, cascade deletes configured\n\n"
            "4. **Progress Tracking Flow:**\n"
            "   - GET /api/progress?user_id=1\n"
            "   - Returns current course, module, lesson\n"
            "   - Shows streak days, total time, completion %\n"
            "   - Verify: Data matches database state\n\n"
            "**Testing Method:**\n"
            "- Trace data flow through code (don't actually run, just analyze)\n"
            "- Check API contracts match between frontend and backend\n"
            "- Verify database schema supports all flows\n"
            "- Identify missing endpoints or incomplete implementations\n\n"
            "**Output:** Integration test report with:\n"
            "- Flow-by-flow analysis\n"
            "- Data flow diagrams (text-based)\n"
            "- Gaps or broken integrations\n"
            "- Fixes needed (API changes, model updates, etc.)\n"
        ),
        expected_output=(
            "An integration validation report including:\n"
            "- Test scenario results (pass/fail for each)\n"
            "- Data flow analysis for each user journey\n"
            "- API contract mismatches found\n"
            "- Database schema issues\n"
            "- List of integration bugs with fixes\n"
            "(Target: 1000-1200 words)"
        ),
        agent=integration_validator,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "integration_validation_report.md"),
        context=[task_validate_backend, task_validate_frontend]
    )

    task_validate_data = Task(
        description=(
            "Validate that demo data aligns with curriculum design documents and is complete.\n\n"
            "**Validation Checks:**\n\n"
            "1. **Alignment with Curriculum Scaffold** (curriculum_scaffold.md):\n"
            "   - Module 1 title matches: 'Foundations of AI & Machine Learning'\n"
            "   - Duration: 6-8 weeks (check seed_data.py sets 8 weeks)\n"
            "   - Week 1 topics match: Python, AI taxonomy, NumPy, Pandas, Matplotlib\n"
            "   - Learning outcomes from scaffold appear in Course model\n\n"
            "2. **Alignment with Learning Objectives** (learning_objectives.md):\n"
            "   - Day 1 covers 'Remember: Identify Key Concepts in AI/ML'\n"
            "   - Tasks support Bloom's taxonomy levels\n"
            "   - Activities match instructional design\n\n"
            "3. **Alignment with Instructional Content** (instructional_content_outline.md):\n"
            "   - Day 1 structure: video → reading → hands-on → quiz → reflection\n"
            "   - Duration: ~90 minutes total (check task durations sum correctly)\n"
            "   - Content types match (video+notebook)\n\n"
            "4. **Alignment with Engagement Systems** (engagement_systems.md):\n"
            "   - Streak tracking implemented (Progress model has streak_days)\n"
            "   - Points system exists (DailyTask has points field)\n"
            "   - Micro-commitments: 15-min tasks exist\n\n"
            "5. **Data Completeness:**\n"
            "   - All 5 Day 1 tasks have descriptions\n"
            "   - Quiz questions have correct_answer indices\n"
            "   - Code templates are valid Python\n"
            "   - No NULL values where required\n\n"
            "**Output:** Data validation report listing:\n"
            "- Alignment scores for each design document\n"
            "- Missing or inconsistent data\n"
            "- Recommendations for data improvements\n"
        ),
        expected_output=(
            "A data validation report including:\n"
            "- Curriculum alignment analysis\n"
            "- Content completeness check\n"
            "- Data quality issues found\n"
            "- Recommendations for fixes\n"
            "(Target: 700-900 words)"
        ),
        agent=data_validator,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "data_validation_report.md"),
        context=[task_validate_backend]
    )

    task_generate_fixes = Task(
        description=(
            "Based on all validation reports, create a comprehensive fix plan with code patches.\n\n"
            "**Your Task:**\n"
            "1. Read all validation reports (backend, frontend, integration, data)\n"
            "2. Prioritize bugs: Critical → Major → Minor\n"
            "3. For each bug, generate:\n"
            "   - Root cause analysis\n"
            "   - Exact code fix (full file content or specific Edit commands)\n"
            "   - Test plan to verify fix\n"
            "4. Create implementation sequence (what to fix first)\n\n"
            "**Fix Categories:**\n"
            "- **Critical:** Prevents platform from running (import errors, syntax errors)\n"
            "- **Major:** Breaks core functionality (API crashes, data loss)\n"
            "- **Minor:** UX issues, missing features, optimization\n\n"
            "**Output Format:**\n"
            "For each fix, provide:\n"
            "```\n"
            "## Fix #N: [Title]\n"
            "**Severity:** Critical/Major/Minor\n"
            "**File:** path/to/file.py\n"
            "**Issue:** Brief description\n"
            "**Root Cause:** Why this happened\n"
            "**Fix:**\n"
            "```python\n"
            "# Replace this:\n"
            "old_code = 'example'\n\n"
            "# With this:\n"
            "new_code = 'fixed'\n"
            "```\n"
            "**Testing:** How to verify the fix works\n"
            "```\n\n"
            "Delegate to other agents if needed to deep-dive on complex issues.\n"
        ),
        expected_output=(
            "A comprehensive fix plan document including:\n"
            "- Executive summary (total bugs found, severity breakdown)\n"
            "- Prioritized list of fixes with code\n"
            "- Implementation sequence\n"
            "- Testing recommendations\n"
            "(Target: 1200-1500 words with extensive code examples)"
        ),
        agent=debug_assistant,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "platform_fixes_plan.md"),
        context=[task_validate_backend, task_validate_frontend, task_validate_integration, task_validate_data]
    )

    return [
        task_validate_backend,
        task_validate_frontend,
        task_validate_integration,
        task_validate_data,
        task_generate_fixes
    ]
