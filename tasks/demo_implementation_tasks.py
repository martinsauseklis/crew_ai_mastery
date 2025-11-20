"""Implementation tasks for actually coding the platform (Phase 5)."""

from pathlib import Path
from crewai import Task
from demo_config import DemoConfig


def get_demo_implementation_tasks(
    implementation_architect,
    backend_implementer,
    frontend_implementer,
    devops_implementer
) -> list:
    """Get tasks for Phase 5: Implementation - Actually build the platform (DEMO)."""

    # Output directory for the implemented platform
    platform_dir = DemoConfig.get_demo_artifacts_dir() / "platform_code"
    platform_dir.mkdir(parents=True, exist_ok=True)

    # Subdirectories
    backend_dir = platform_dir / "backend"
    frontend_dir = platform_dir / "frontend"

    task_create_implementation_plan = Task(
        description=(
            "Read the generated design artifacts from artifacts/demo/ including:\n"
            "- system_architecture.md\n"
            "- ux_design.md\n"
            "- data_infrastructure.md\n"
            "- mvp_implementation_plan.md\n\n"
            "Create a detailed implementation plan that breaks down the platform into specific code files:\n"
            "- Backend API structure (routes, models, controllers)\n"
            "- Frontend component structure (pages, components, hooks)\n"
            "- Database schema and migrations\n"
            "- Configuration files\n"
            "- Deployment setup\n\n"
            "Focus on MVP scope: User authentication, course content delivery, progress tracking, "
            "and basic dashboard. Keep it simple but functional.\n\n"
            "Output a clear file structure tree with brief descriptions of each file's purpose."
        ),
        expected_output=(
            "A markdown file 'implementation_plan.md' with:\n"
            "- Complete file structure tree\n"
            "- Description of each major component\n"
            "- Technology choices (Flask/FastAPI, React, SQLite, etc.)\n"
            "- Implementation sequence (which files to create first)\n"
            "(Target: ~600-800 words)"
        ),
        agent=implementation_architect,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "implementation_plan.md")
    )

    task_implement_backend = Task(
        description=(
            "Based on the implementation plan and design artifacts, write the backend code:\n\n"
            "Create a Flask/FastAPI application with:\n"
            "1. **app.py** - Main application entry point with API routes\n"
            "2. **models.py** - SQLAlchemy database models (User, Course, Module, Progress, etc.)\n"
            "3. **auth.py** - Authentication and authorization logic\n"
            "4. **config.py** - Application configuration\n"
            "5. **database.py** - Database setup and initialization\n"
            "6. **requirements.txt** - Python dependencies\n\n"
            "Write COMPLETE, RUNNABLE code files. Include:\n"
            "- Proper imports\n"
            "- Error handling\n"
            "- Input validation\n"
            "- Comments explaining key sections\n"
            "- RESTful API endpoints for: /api/auth, /api/courses, /api/progress, /api/user\n\n"
            "Keep it simple but functional. This should be deployable code that actually works.\n\n"
            "CRITICAL FORMAT REQUIREMENTS:\n"
            "- DO NOT wrap your entire output in a markdown code block\n"
            "- Start directly with the heading\n"
            "- Use this EXACT format for each file:\n\n"
            "## app.py\n"
            "```python\n"
            "# Complete code here\n"
            "```\n\n"
            "## requirements.txt\n"
            "```text\n"
            "fastapi\n"
            "uvicorn\n"
            "```\n\n"
            "The filename MUST appear as a heading (##) immediately before each code block.\n"
            "Start your response directly with: ## app.py (no markdown wrapper!)"
        ),
        expected_output=(
            "A markdown file 'backend_implementation.md' containing:\n"
            "- Complete code for all backend files\n"
            "- Each file in a separate code block with filename header\n"
            "- Brief setup instructions\n"
            "(Target: Complete working backend code)"
        ),
        agent=backend_implementer,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "backend_implementation.md"),
        context=[task_create_implementation_plan]
    )

    task_implement_frontend = Task(
        description=(
            "Based on the implementation plan, UX design, and backend API, write the frontend code:\n\n"
            "Create a React/Next.js application with:\n"
            "1. **pages/** - Main pages (Home, Login, Dashboard, Course, Profile)\n"
            "2. **components/** - Reusable components (CourseCard, ProgressBar, Navigation, etc.)\n"
            "3. **lib/** - Utility functions and API client\n"
            "4. **styles/** - Global styles and CSS\n"
            "5. **package.json** - Dependencies\n\n"
            "Write COMPLETE, RUNNABLE code files. Include:\n"
            "- React components with hooks\n"
            "- API integration (fetch calls to backend)\n"
            "- Responsive design\n"
            "- Basic styling (can use Tailwind CSS)\n"
            "- Routing configuration\n\n"
            "Focus on these key pages:\n"
            "- Login/Register page\n"
            "- Dashboard (shows enrolled courses and progress)\n"
            "- Course view (displays modules and lessons)\n"
            "- Profile page (user settings)\n\n"
            "CRITICAL FORMAT REQUIREMENTS:\n"
            "- DO NOT wrap your entire output in a markdown code block\n"
            "- Start directly with the heading\n"
            "- Use this EXACT format for each file:\n\n"
            "## pages/index.tsx\n"
            "```typescript\n"
            "// Complete code here\n"
            "```\n\n"
            "## package.json\n"
            "```json\n"
            "{ dependencies }\n"
            "```\n\n"
            "The filename MUST appear as a heading (##) immediately before each code block.\n"
            "Start your response directly with: ## pages/ (no markdown wrapper!)"
        ),
        expected_output=(
            "A markdown file 'frontend_implementation.md' containing:\n"
            "- Complete code for all frontend files\n"
            "- Each file in a separate code block with filename header\n"
            "- Component hierarchy overview\n"
            "(Target: Complete working frontend code)"
        ),
        agent=frontend_implementer,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "frontend_implementation.md"),
        context=[task_create_implementation_plan, task_implement_backend]
    )

    task_create_deployment_setup = Task(
        description=(
            "Create deployment and setup files to make the platform easy to run:\n\n"
            "You MUST create these EXACT files:\n"
            "1. **docker-compose.yml** - Complete Docker Compose configuration with backend, frontend, and database services\n"
            "2. **backend/Dockerfile** - Backend containerization (Python/FastAPI)\n"
            "3. **frontend/Dockerfile** - Frontend containerization (Node/React)\n"
            "4. **.env.example** - ALL environment variables with examples and descriptions\n"
            "5. **setup.sh** - Automated setup script that validates prerequisites and copies .env\n"
            "6. **README.md** - COMPREHENSIVE setup guide (see requirements below)\n\n"
            "README.md MUST include ALL these sections with step-by-step instructions:\n"
            "1. **Project Overview** - What this platform does\n"
            "2. **Prerequisites** - Docker, Docker Compose, Node.js, Python versions\n"
            "3. **Quick Start** - 3 commands to run: cp .env.example .env, edit .env, docker-compose up\n"
            "4. **Environment Configuration** - Detailed explanation of each .env variable\n"
            "5. **Running with Docker** - Step by step with expected output\n"
            "6. **Local Development Setup** - How to run backend and frontend separately without Docker\n"
            "7. **Testing the Platform** - How to verify it's working (URLs to visit, test accounts)\n"
            "8. **Common Issues & Solutions** - At least 5 troubleshooting scenarios\n"
            "9. **Project Structure** - Directory tree showing what's where\n"
            "10. **API Documentation** - List of available endpoints\n\n"
            ".env.example MUST include:\n"
            "- DATABASE_URL with example\n"
            "- SECRET_KEY\n"
            "- POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB\n"
            "- Any API keys needed (OpenAI, Anthropic, etc.)\n"
            "- FRONTEND_URL and BACKEND_URL\n"
            "- Comments explaining each variable\n\n"
            "CRITICAL FORMAT REQUIREMENTS:\n"
            "- DO NOT wrap your entire output in a markdown code block\n"
            "- Start directly with the heading\n"
            "- Use this EXACT format for each file:\n\n"
            "## docker-compose.yml\n"
            "```yaml\n"
            "version: '3.8'\n"
            "services:...\n"
            "```\n\n"
            "## backend/Dockerfile\n"
            "```dockerfile\n"
            "FROM python:3.9\n"
            "...\n"
            "```\n\n"
            "## frontend/Dockerfile\n"
            "```dockerfile\n"
            "FROM node:14\n"
            "...\n"
            "```\n\n"
            "## .env.example\n"
            "```bash\n"
            "DATABASE_URL=...\n"
            "```\n\n"
            "## setup.sh\n"
            "```bash\n"
            "#!/bin/bash\n"
            "...\n"
            "```\n\n"
            "## README.md\n"
            "```markdown\n"
            "# AI Mastery Platform\n"
            "[ALL 10 sections here]\n"
            "```\n\n"
            "The filename MUST appear as a heading (##) immediately before each code block.\n"
            "Start your response directly with: ## docker-compose.yml (no wrapping code block!)\n"
            "Verify your output includes ALL 6 files with complete, copy-paste-ready content."
        ),
        expected_output=(
            "A markdown file 'deployment_setup.md' containing:\n"
            "- docker-compose.yml (complete, production-ready)\n"
            "- backend/Dockerfile (complete)\n"
            "- frontend/Dockerfile (complete)\n"
            "- .env.example (complete with ALL variables and comments)\n"
            "- setup.sh script (complete with prerequisite validation)\n"
            "- README.md with ALL 10 required sections (minimum 100 lines)\n"
            "(Target: Everything needed for immediate deployment)"
        ),
        agent=devops_implementer,
        output_file=str(DemoConfig.get_demo_artifacts_dir() / "deployment_setup.md"),
        context=[task_implement_backend, task_implement_frontend]
    )

    return [
        task_create_implementation_plan,
        task_implement_backend,
        task_implement_frontend,
        task_create_deployment_setup
    ]
