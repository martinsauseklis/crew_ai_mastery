"""
Elite Software Development Crew - Main Orchestration Script
============================================================
This is the main entry point for running the development crew.
It orchestrates all agents and tasks to build a complete web application.
"""

import os
import sys
from pathlib import Path
from crewai import Crew, Process
import yaml
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

from agents import create_all_agents
from tasks import create_all_tasks


def load_config() -> dict:
    """Load the main crew configuration."""
    config_path = Path(__file__).parent / "crew_config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def setup_environment():
    """Set up environment and check prerequisites."""
    # Load environment variables
    load_dotenv()

    # Check for required environment variables
    required_vars = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            f"Please set them in your .env file.\n\n"
            f"Required:\n"
            f"  OPENAI_API_KEY - for GPT-4o agents (Product, Architecture, Docs)\n"
            f"  ANTHROPIC_API_KEY - for Claude Sonnet 4.5 agents (Coding, QA)\n"
        )

    # Create output directory structure
    output_dir = Path("output")
    directories = [
        "docs",
        "app",
        "components",
        "lib",
        "prisma",
        "tests",
        "scripts",
        "public",
        ".github",
    ]

    for directory in directories:
        (output_dir / directory).mkdir(parents=True, exist_ok=True)

    print("[OK] Environment setup complete")


def get_multiline_input(prompt: str) -> str:
    """Get multiline input from user. End with empty line."""
    print(f"\n{prompt}")
    print("(Enter your text. Press Enter twice when done)\n")
    lines = []
    empty_count = 0

    while True:
        try:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                lines.append(line)
        except EOFError:
            break

    return "\n".join(lines).strip()


def get_list_input(prompt: str) -> list:
    """Get list input from user (one item per line, empty line to finish)."""
    print(f"\n{prompt}")
    print("(One item per line. Press Enter twice when done)\n")
    items = []
    empty_count = 0

    while True:
        try:
            line = input("- ")
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                items.append(line.strip())
        except EOFError:
            break

    return items


def collect_project_requirements() -> str:
    """
    Interactive prompt to collect structured project requirements.
    Returns a formatted project brief.
    """
    print("\n" + "=" * 80)
    print("ELITE SOFTWARE DEVELOPMENT CREW - PROJECT REQUIREMENTS")
    print("=" * 80)
    print("\nLet's define your project requirements in a structured format.")
    print("This ensures the crew has all the information needed for success.\n")

    # Project Name
    print("\n[PROJECT NAME]:")
    project_name = input("Enter project name: ").strip()

    # Purpose
    purpose = get_multiline_input(
        "[PURPOSE / WHY THIS EXISTS]:\n"
        "Describe the main goal -- the outcome, not the solution."
    )

    # Target Users
    target_users = get_multiline_input(
        "[TARGET USERS]:\n"
        "Who will use this? Roles, demographics, needs."
    )

    # User Problem
    user_problem = get_multiline_input(
        "[USER PROBLEM]:\n"
        "Explain what they are struggling with today."
    )

    # Success Metrics
    success_metrics = get_list_input(
        "[SUCCESS METRICS / KPIs]:\n"
        "Examples:\n"
        "  - Reduce onboarding friction\n"
        "  - Users can complete task in < 2 minutes\n"
        "  - Must score >=95 Lighthouse performance"
    )

    # Functional Requirements
    functional_reqs = get_list_input(
        "[FUNCTIONAL REQUIREMENTS]:\n"
        "List all required capabilities"
    )

    # Nice-to-Haves
    nice_to_haves = get_list_input(
        "[NICE-TO-HAVES] (not mandatory):\n"
        "List optional enhancements"
    )

    # System Constraints
    print("\n[SYSTEM CONSTRAINTS]:")
    print("Default constraints (press Enter to accept or type custom):")
    print("  - Must use Next.js + Node + Prisma + PostgreSQL")
    print("  - Must use secure authentication (NextAuth)")
    print("  - Must support local hosting")

    custom_constraints = input("\nAdd additional constraints (or press Enter to skip): ").strip()
    system_constraints = [
        "Must use Next.js + Node + Prisma + PostgreSQL",
        "Must use secure authentication (NextAuth)",
        "Must support local hosting"
    ]
    if custom_constraints:
        system_constraints.append(custom_constraints)

    # Security Requirements
    security_reqs = get_list_input(
        "[SECURITY REQUIREMENTS]:\n"
        "Examples:\n"
        "  - Hashed passwords\n"
        "  - Role-based access control\n"
        "  - MFA support"
    )

    # Testing & Quality
    print("\n[TESTING & QUALITY REQUIREMENTS]:")
    print("Default requirements (automatically included):")
    print("  - 100% critical-path coverage")
    print("  - E2E tests via Playwright")
    print("  - Must meet WCAG 2.1 AA")
    print("  - Test coverage >80%")

    additional_quality = input("\nAdd additional quality requirements (or press Enter to skip): ").strip()
    testing_reqs = [
        "100% critical-path coverage",
        "E2E tests via Playwright",
        "Must meet WCAG 2.1 AA",
        "Test coverage >80%"
    ]
    if additional_quality:
        testing_reqs.append(additional_quality)

    # Output Expectations
    print("\n[OUTPUT EXPECTATIONS]:")
    print("The crew will automatically deliver:")
    print("  - Complete project structure")
    print("  - Full code implementation")
    print("  - Comprehensive documentation")
    print("  - Test coverage")
    print("  - Quality reports")
    print("  - Report on tradeoffs and unresolved assumptions")

    # Open Questions
    open_questions = get_list_input(
        "[OPEN QUESTIONS] (crew should resolve):\n"
        "List anything unclear or unknown"
    )

    # Format the brief
    brief = f"""
# {project_name}

## Purpose / Why This Exists
{purpose}

## Target Users
{target_users}

## User Problem
{user_problem}

## Success Metrics / KPIs
{chr(10).join(f'- {metric}' for metric in success_metrics)}

## Functional Requirements
{chr(10).join(f'- {req}' for req in functional_reqs)}

## Nice-to-Haves (Not Mandatory)
{chr(10).join(f'- {nice}' for nice in nice_to_haves) if nice_to_haves else '- None specified'}

## System Constraints
{chr(10).join(f'- {constraint}' for constraint in system_constraints)}

## Security Requirements
{chr(10).join(f'- {req}' for req in security_reqs)}

## Testing & Quality Requirements
{chr(10).join(f'- {req}' for req in testing_reqs)}

## Output Expectations
The crew should deliver:
- Complete project structure following Next.js best practices
- Full code implementation with TypeScript
- Comprehensive documentation (README, API docs, setup guides)
- Test coverage (unit, integration, E2E)
- Quality reports (accessibility, performance, security)
- Deployment configuration (Docker, CI/CD)
- Report on architectural decisions and tradeoffs

## Open Questions (Crew Should Resolve)
{chr(10).join(f'- {question}' for question in open_questions) if open_questions else '- None specified'}

## Technical Stack (Pre-defined)
- Frontend: Next.js 14+ (App Router, React Server Components)
- Backend: Node.js (API Routes, Server Actions)
- Database: PostgreSQL
- ORM: Prisma
- Authentication: NextAuth.js
- Testing: Jest + Playwright
- Styling: Tailwind CSS
- Containerization: Docker + Docker Compose
- CI/CD: GitHub Actions
"""

    return brief


def save_brief_to_file(brief: str, filename: str = "project_brief.txt"):
    """Save the project brief to a file."""
    output_path = Path(filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(brief)
    print(f"\n[OK] Project brief saved to: {output_path.absolute()}")


def create_crew(project_brief: str) -> Crew:
    """
    Create and configure the development crew.

    Each agent automatically uses the optimal model for their role:
    - Coding (Backend/Frontend/DevOps): Claude Sonnet 4.5
    - QA/Testing: Claude Sonnet 4.5
    - Strategy/Architecture/Review: GPT-4o
    - Design/Documentation: GPT-4o

    Args:
        project_brief: The project description and requirements

    Returns:
        Configured Crew instance
    """
    # Create all agents (each with optimal model)
    print("Creating agents...")
    print("  - Coding agents: Claude Sonnet 4.5")
    print("  - Strategy agents: GPT-4o")
    print("  - Documentation agents: GPT-4o")
    agents = create_all_agents()
    print(f"[OK] Created {len(agents)} specialized agents")

    # Create all tasks
    print("Creating tasks...")
    tasks = create_all_tasks(agents)
    print(f"[OK] Created {len(tasks)} tasks")

    # Load crew configuration
    config = load_config()

    # Create crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,  # Tasks run in order
        verbose=True,
        memory=True,  # Enable memory for context retention
        embedder={
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small"
            }
        }
    )

    print("[OK] Crew assembled and ready")
    return crew


def run_crew(project_brief: str):
    """
    Run the complete development crew workflow.

    Args:
        project_brief: The project description and requirements

    Returns:
        Final output from the crew
    """
    print("\n" + "=" * 80)
    print("ELITE SOFTWARE DEVELOPMENT CREW")
    print("=" * 80)
    print()

    # Setup
    print("Setting up environment...")
    setup_environment()
    print()

    # Create crew
    crew = create_crew(project_brief)
    print()

    # Run crew
    print("=" * 80)
    print("STARTING DEVELOPMENT WORKFLOW")
    print("=" * 80)
    print()
    print("Project Brief:")
    print("-" * 80)
    print(project_brief)
    print("-" * 80)
    print()

    # Execute workflow
    inputs = {
        "project_brief": project_brief,
        "tech_stack": {
            "frontend": "Next.js 14+ (App Router, React Server Components)",
            "backend": "Node.js (API Routes, Server Actions)",
            "database": "PostgreSQL",
            "orm": "Prisma",
            "authentication": "NextAuth.js",
            "testing": "Jest + Playwright",
            "styling": "Tailwind CSS",
        }
    }

    result = crew.kickoff(inputs=inputs)

    print()
    print("=" * 80)
    print("WORKFLOW COMPLETE")
    print("=" * 80)
    print()

    return result


def main():
    """Main entry point."""
    print("\n" + "=" * 80)
    print("ELITE SOFTWARE DEVELOPMENT CREW")
    print("=" * 80)

    # Check if brief file is provided as argument
    if len(sys.argv) > 1:
        brief_file = sys.argv[1]
        if Path(brief_file).exists():
            with open(brief_file, "r", encoding="utf-8") as f:
                project_brief = f.read()
            print(f"\n[OK] Loaded project brief from: {brief_file}")
        else:
            print(f"\n[ERROR] File not found: {brief_file}")
            print("Falling back to interactive mode...")
            project_brief = collect_project_requirements()
            save_brief_to_file(project_brief)
    else:
        # Interactive mode
        print("\nNo brief file provided. Starting interactive mode...")
        project_brief = collect_project_requirements()

        # Ask if user wants to save the brief
        print("\n" + "-" * 80)
        save_choice = input("\nSave this brief to file? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = input("Filename (default: project_brief.txt): ").strip()
            if not filename:
                filename = "project_brief.txt"
            save_brief_to_file(project_brief, filename)

    # Confirm before running
    print("\n" + "=" * 80)
    print("READY TO START")
    print("=" * 80)
    print("\nThe crew will now begin building your application.")
    print("This process may take 20-60 minutes depending on complexity.")
    print("\nModel assignments (optimized for each role):")
    print("  - Coding: Claude Sonnet 4.5 (Backend, Frontend, DevOps, QA)")
    print("  - Strategy: GPT-4o (Product, Architecture, Tech Lead)")
    print("  - Documentation: GPT-4o (UX, Docs)")
    print("\nEstimated cost: $15-60 (using optimal models)")

    confirm = input("\nProceed with development? (y/n): ").strip().lower()
    if confirm != 'y':
        print("\nCancelled by user. Your brief has been saved for later use.")
        sys.exit(0)

    # Run crew
    try:
        result = run_crew(project_brief)

        print()
        print("=" * 80)
        print("FINAL OUTPUT")
        print("=" * 80)
        print()
        print(result)
        print()

        print("[OK] All files generated in: output/")
        print()
        print("Next steps:")
        print("1. Review output/docs/README.md for project overview")
        print("2. Follow output/docs/SETUP.md to set up development environment")
        print("3. Review output/docs/FINAL_REVIEW.md for quality assessment")
        print()

    except KeyboardInterrupt:
        print("\n\nWorkflow interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError running crew: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
