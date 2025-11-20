#!/usr/bin/env python3
"""
AI Mastery Platform - Demo Mode

Runs a simplified version of the full platform to demonstrate all agents,
crews, and tasks with reduced output expectations for faster evaluation.

Usage:
    python run_demo.py
"""

import sys
import time
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.live import Live
from rich import box

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.config import Config
from core import StateManager, LLMClient
from demo_config import DemoConfig
from demo_profile import get_demo_user_profile
from crews.demo_crews import (
    run_demo_strategy_crew,
    run_demo_curriculum_crew,
    run_demo_platform_crew,
    run_demo_qa_crew,
    run_demo_implementation_crew
)
from utils.extract_platform_code import extract_and_build_platform
from utils.artifact_checker import all_phase_artifacts_exist, get_missing_artifacts


console = Console()


def print_welcome():
    """Print welcome message."""
    console.print()
    console.print(Panel.fit(
        "[bold cyan]AI MASTERY PLATFORM[/bold cyan]\n"
        "[bold yellow]DEMO MODE[/bold yellow]\n\n"
        "[dim]Fast evaluation of all agents, crews, and tasks[/dim]",
        border_style="cyan",
        box=box.DOUBLE
    ))
    console.print()

    console.print("[bold]What you'll see:[/bold]")
    console.print("  • 17 specialized agents in action")
    console.print("  • 5 crews executing sequentially")
    console.print("  • 21 tasks generating artifacts + ACTUAL CODE")
    console.print()
    console.print("[dim]Estimated time: 15-20 minutes[/dim]")
    console.print("[dim]Estimated cost: $8-15[/dim]")
    console.print()


def print_agents_overview():
    """Print overview of all agents."""
    console.print()
    console.print(Panel("[bold]Initializing 17 Specialized Agents[/bold]", border_style="blue"))

    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
    table.add_column("Division", style="cyan")
    table.add_column("Agent", style="yellow")
    table.add_column("Model", style="dim")

    agents_data = [
        ("Executive", "Chief of Staff", "Claude Sonnet 4.5"),
        ("Learning R&D", "Curriculum Architect", "Claude Sonnet 4.5"),
        ("Learning R&D", "AI Subject Matter Expert", "GPT-4o"),
        ("Learning R&D", "Instructional Designer", "Claude Sonnet 4.5"),
        ("Learning R&D", "Cognitive Scientist", "Claude Sonnet 4.5"),
        ("Learning R&D", "Behavior Designer", "Claude Sonnet 4.5"),
        ("Product", "Product Manager", "GPT-4o"),
        ("Product", "UX Designer", "Claude Sonnet 4.5"),
        ("Engineering", "Full-Stack Developer", "GPT-4o"),
        ("Engineering", "Backend Engineer", "GPT-4o"),
        ("Engineering", "ML Engineer", "GPT-4o"),
        ("Engineering", "LLM Engineer", "GPT-4o"),
        ("QA", "QA Researcher", "Claude Sonnet 4.5"),
        ("Implementation", "Implementation Architect", "GPT-4o"),
        ("Implementation", "Backend Implementer", "GPT-4o"),
        ("Implementation", "Frontend Implementer", "GPT-4o"),
        ("Implementation", "DevOps Implementer", "GPT-4o"),
    ]

    for division, agent, model in agents_data:
        table.add_row(division, agent, model)

    console.print(table)
    console.print()


def run_phase_with_progress(phase_num, phase_name, phase_key, crew_func, state_manager, llm_client):
    """Run a crew phase with progress indicator, checking artifacts first."""
    console.print()
    console.print(Panel(
        f"[bold]PHASE {phase_num}: {phase_name}[/bold]",
        border_style="green"
    ))

    # Check if all artifacts already exist BEFORE starting crew
    if all_phase_artifacts_exist(phase_key):
        console.print(f"[dim]All {phase_name} artifacts exist - skipping crew execution[/dim]")
        console.print(f"[green]OK Phase {phase_num} completed (skipped - artifacts exist) in 0.0s[/green]")
        return {
            "status": "success",
            "crew_name": f"Demo{phase_name.replace(' ', '')}",
            "skipped": True,
            "result": "Skipped - all artifacts exist"
        }, 0.0

    # Check which artifacts are missing
    missing = get_missing_artifacts(phase_key)
    if missing:
        console.print(f"[dim]Missing artifacts: {', '.join(missing)}[/dim]")

    start_time = time.time()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        task = progress.add_task(f"[cyan]Running {phase_name}...", total=None)

        try:
            result = crew_func(state_manager, llm_client)

            elapsed = time.time() - start_time

            if result["status"] == "success":
                progress.update(task, description=f"[green]OK {phase_name} completed")
                console.print(f"[green]OK Phase {phase_num} completed in {elapsed:.1f}s[/green]")
                return result, elapsed
            else:
                progress.update(task, description=f"[red]FAIL {phase_name} failed")
                console.print(f"[red]FAIL Phase {phase_num} failed: {result.get('error', 'Unknown error')}[/red]")
                return result, elapsed

        except Exception as e:
            elapsed = time.time() - start_time
            console.print(f"[red]FAIL Phase {phase_num} error: {str(e)}[/red]")
            return {"status": "failed", "error": str(e)}, elapsed


def print_summary(results, total_time, llm_client):
    """Print execution summary."""
    console.print()
    console.print(Panel.fit(
        "[bold green]DEMO COMPLETE[/bold green]",
        border_style="green",
        box=box.DOUBLE
    ))

    # Summary table
    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
    table.add_column("Phase", style="cyan")
    table.add_column("Crew", style="yellow")
    table.add_column("Status", style="bold")
    table.add_column("Time", justify="right")

    for result, elapsed in results:
        status_icon = "✓" if result["status"] == "success" else "✗"
        status_color = "green" if result["status"] == "success" else "red"
        status = f"[{status_color}]{status_icon} {result['status'].capitalize()}[/{status_color}]"

        phase_match = result["crew_name"].replace("Demo", "").replace("Crew", "")
        table.add_row(
            phase_match,
            result["crew_name"],
            status,
            f"{elapsed:.1f}s"
        )

    console.print(table)

    # Stats
    console.print()
    successful = sum(1 for r, _ in results if r["status"] == "success")
    total_phases = len(results)

    stats_table = Table.grid(padding=(0, 2))
    stats_table.add_column(style="bold cyan")
    stats_table.add_column(style="white")

    stats_table.add_row("Agents Executed:", "17")
    stats_table.add_row("Crews Completed:", f"{successful}/{total_phases}")
    stats_table.add_row("Tasks Finished:", "21" if successful == total_phases else f"~{successful * 4}")
    stats_table.add_row("Total Time:", f"{total_time:.1f}s ({total_time/60:.1f} min)")

    # Try to get cost info
    try:
        from core.logging_utils import get_total_cost_summary
        cost_summary = get_total_cost_summary()
        if cost_summary and cost_summary.get("total_cost", 0) > 0:
            stats_table.add_row("Total Cost:", f"${cost_summary['total_cost']:.2f}")
    except:
        stats_table.add_row("Total Cost:", "See logs/llm_calls.jsonl")

    stats_table.add_row("Artifacts:", f"artifacts/demo/ (21 files + code)")

    console.print(Panel(stats_table, title="[bold]Summary[/bold]", border_style="cyan"))

    # Next steps
    console.print()
    console.print("[bold]Next Steps:[/bold]")
    console.print("  1. Navigate to platform: [cyan]cd artifacts/demo/platform_code[/cyan]")
    console.print("  2. Review the code: [cyan]ls -R[/cyan]")
    console.print("  3. Setup and run: [cyan]cp .env.example .env && docker-compose up[/cyan]")
    console.print("  4. Or run locally: See [cyan]README.md[/cyan] in platform_code/")
    console.print("  5. View design docs: [cyan]ls artifacts/demo/*.md[/cyan]")
    console.print()


def main():
    """Main demo execution."""
    try:
        # Welcome
        print_welcome()

        # Initialize system
        console.print("[bold]Initializing system...[/bold]")
        Config.ensure_directories()
        DemoConfig.ensure_demo_directories()
        Config.validate_api_keys()

        state_manager = StateManager()
        llm_client = LLMClient()

        console.print("[green]✓ System initialized[/green]")

        # Collect user profile
        user_profile = get_demo_user_profile()
        Config.set_user_profile(user_profile)

        # Show agents
        print_agents_overview()

        # Confirm start
        console.print()
        response = console.input("[bold yellow]Ready to start demo? (y/n):[/bold yellow] ")
        if response.lower() != 'y':
            console.print("[yellow]Demo cancelled.[/yellow]")
            return

        # Track results
        results = []
        start_time = time.time()

        # Phase 1: Strategy
        result, elapsed = run_phase_with_progress(
            1, "Strategy Crew", "strategy",
            run_demo_strategy_crew,
            state_manager, llm_client
        )
        results.append((result, elapsed))

        if result["status"] != "success" and not result.get("skipped"):
            console.print("[red]Phase 1 failed. Stopping demo.[/red]")
            return

        # Phase 2: Curriculum
        result, elapsed = run_phase_with_progress(
            2, "Curriculum Crew", "curriculum",
            run_demo_curriculum_crew,
            state_manager, llm_client
        )
        results.append((result, elapsed))

        if result["status"] != "success" and not result.get("skipped"):
            console.print("[red]Phase 2 failed. Stopping demo.[/red]")
            return

        # Phase 3: Platform
        result, elapsed = run_phase_with_progress(
            3, "Platform Crew", "platform",
            run_demo_platform_crew,
            state_manager, llm_client
        )
        results.append((result, elapsed))

        if result["status"] != "success" and not result.get("skipped"):
            console.print("[red]Phase 3 failed. Stopping demo.[/red]")
            return

        # Phase 4: QA
        result, elapsed = run_phase_with_progress(
            4, "QA Crew", "qa",
            run_demo_qa_crew,
            state_manager, llm_client
        )
        results.append((result, elapsed))

        if result["status"] != "success" and not result.get("skipped"):
            console.print("[red]Phase 4 failed. Stopping demo.[/red]")
            return

        # Phase 5: Implementation - Actually build the platform!
        console.print()
        console.print("[bold yellow]━━━ NOW BUILDING THE ACTUAL PLATFORM CODE ━━━[/bold yellow]")
        console.print()

        result, elapsed = run_phase_with_progress(
            5, "Implementation Crew", "implementation",
            run_demo_implementation_crew,
            state_manager, llm_client
        )
        results.append((result, elapsed))

        # Extract platform code from markdown files (always if Phase 5 artifacts exist)
        if result["status"] == "success":
            console.print()
            console.print("[bold cyan]━━━ EXTRACTING PLATFORM CODE TO FILES ━━━[/bold cyan]")
            console.print()

            try:
                demo_artifacts_dir = DemoConfig.get_demo_artifacts_dir()
                platform_code_dir = demo_artifacts_dir / "platform_code"

                # Check if platform_code already has files
                if platform_code_dir.exists() and any(platform_code_dir.iterdir()):
                    console.print("[dim]Platform code directory already exists with files[/dim]")
                    console.print("[yellow]Skipping extraction (delete platform_code/ to re-extract)[/yellow]")
                else:
                    extract_and_build_platform(demo_artifacts_dir, platform_code_dir)
                    console.print("[bold green]SUCCESS: Platform code extracted and ready to run![/bold green]")
                    console.print(f"[dim]Location: {platform_code_dir}[/dim]")
            except Exception as e:
                console.print(f"[red]Warning: Failed to extract platform code: {e}[/red]")
                console.print("[yellow]You can extract manually later using: python utils/extract_platform_code.py[/yellow]")

        # Calculate total time
        total_time = time.time() - start_time

        # Print summary
        print_summary(results, total_time, llm_client)

    except KeyboardInterrupt:
        console.print("\n[yellow]Demo interrupted by user.[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        import traceback
        console.print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
