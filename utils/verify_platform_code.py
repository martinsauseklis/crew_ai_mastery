"""
Verify that all required platform code files exist.

This script checks if the extracted platform code is complete and ready to run.
"""

from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def verify_platform_code(platform_dir: Path) -> bool:
    """Verify all required files exist."""

    required_files = {
        # Root level
        "docker-compose.yml": "Docker Compose configuration",
        ".env.example": "Environment variables template",
        "README.md": "Setup instructions (min 100 lines)",
        "setup.sh": "Setup script",

        # Backend
        "backend/Dockerfile": "Backend container definition",
        "backend/app.py": "Backend application entry point",
        "backend/main.py": "Alternative backend entry point",
        "backend/models.py": "Database models",
        "backend/auth.py": "Authentication logic",
        "backend/config.py": "Configuration",
        "backend/database.py": "Database setup",
        "backend/requirements.txt": "Python dependencies",

        # Frontend
        "frontend/Dockerfile": "Frontend container definition",
        "frontend/package.json": "Node.js dependencies",
        "frontend/src/pages/index.js": "Home page",
        "frontend/src/pages/login.js": "Login page",
        "frontend/src/pages/dashboard.js": "Dashboard page",
        "frontend/src/components/": "Components directory",
        "frontend/src/lib/": "Utility library",
    }

    console.print()
    console.print("[bold cyan]Platform Code Verification[/bold cyan]")
    console.print()

    if not platform_dir.exists():
        console.print(f"[red]ERROR: Platform directory not found: {platform_dir}[/red]")
        return False

    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
    table.add_column("File/Directory", style="white")
    table.add_column("Status", style="bold")
    table.add_column("Description", style="dim")

    missing_files = []
    critical_missing = []

    for file_path, description in required_files.items():
        full_path = platform_dir / file_path

        # Check if it's a directory or file
        if file_path.endswith("/"):
            exists = full_path.exists() and full_path.is_dir()
        else:
            exists = full_path.exists()

        if exists:
            # Check README.md has minimum 100 lines
            if file_path == "README.md":
                line_count = len(full_path.read_text(encoding='utf-8').splitlines())
                if line_count < 100:
                    status = f"[yellow]WARN Only {line_count} lines[/yellow]"
                    missing_files.append(f"{file_path} (incomplete: {line_count}/100 lines)")
                else:
                    status = f"[green]OK ({line_count} lines)[/green]"
            else:
                status = "[green]OK Found[/green]"
        else:
            # Check if alternative exists (e.g., app.py vs main.py)
            if file_path == "backend/app.py":
                alt_path = platform_dir / "backend" / "main.py"
                if alt_path.exists():
                    status = "[green]OK Found (main.py)[/green]"
                    exists = True
                else:
                    status = "[red]MISSING[/red]"
                    missing_files.append(file_path)
                    critical_missing.append(file_path)
            elif file_path == "backend/main.py":
                # Skip if app.py exists
                app_path = platform_dir / "backend" / "app.py"
                if app_path.exists():
                    continue
                status = "[yellow]Optional[/yellow]"
            else:
                status = "[red]MISSING[/red]"
                missing_files.append(file_path)

                # Mark critical files
                if file_path in [
                    "docker-compose.yml",
                    ".env.example",
                    "backend/Dockerfile",
                    "backend/requirements.txt",
                    "frontend/Dockerfile",
                    "frontend/package.json"
                ]:
                    critical_missing.append(file_path)

        table.add_row(file_path, status, description)

    console.print(table)
    console.print()

    # Check for common naming issues
    env_example_alt = platform_dir / "env.example"
    if env_example_alt.exists() and not (platform_dir / ".env.example").exists():
        console.print("[yellow]WARN Found 'env.example' instead of '.env.example' (wrong name)[/yellow]")
        console.print(f"  Fix: Rename {env_example_alt} to .env.example")
        console.print()

    # Summary
    if not missing_files:
        console.print("[bold green]SUCCESS All required files found! Platform is ready to run.[/bold green]")
        console.print()
        console.print("[bold]Next steps:[/bold]")
        console.print(f"  1. cd {platform_dir}")
        console.print("  2. cp .env.example .env")
        console.print("  3. Edit .env with your settings")
        console.print("  4. docker-compose up")
        console.print()
        return True
    else:
        console.print(f"[yellow]WARN Found {len(missing_files)} missing files/issues:[/yellow]")
        for file in missing_files:
            console.print(f"  - {file}")
        console.print()

        if critical_missing:
            console.print("[bold red]FAIL Critical files missing (platform won't run):[/bold red]")
            for file in critical_missing:
                console.print(f"  - {file}")
            console.print()

        console.print("[bold]To fix:[/bold]")
        console.print("  1. Delete Phase 5 artifacts:")
        console.print("     rm artifacts/demo/implementation_plan.md")
        console.print("     rm artifacts/demo/backend_implementation.md")
        console.print("     rm artifacts/demo/frontend_implementation.md")
        console.print("     rm artifacts/demo/deployment_setup.md")
        console.print()
        console.print("  2. Delete platform_code to force re-extraction:")
        console.print("     rm -rf artifacts/demo/platform_code")
        console.print()
        console.print("  3. Regenerate with fixed format requirements:")
        console.print("     python run_demo.py")
        console.print()
        console.print("  (Demo will skip Phases 1-4 and only run Phase 5)")
        console.print()

        return False


def main():
    """Main entry point."""
    import sys

    # Add parent directory to path for imports
    script_dir = Path(__file__).parent.parent
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))

    from demo_config import DemoConfig

    platform_code_dir = DemoConfig.get_demo_artifacts_dir() / "platform_code"

    try:
        success = verify_platform_code(platform_code_dir)
        return 0 if success else 1
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
