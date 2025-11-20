"""
AI Mastery Platform - Multi-Agent Orchestration System

This is the main entry point for running the AI Mastery Platform development crews.
The system orchestrates multiple specialized AI agent crews across 4 phases to design
and plan a comprehensive AI learning platform.
"""

import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pathlib import Path

from core import Config, StateManager, LLMClient, setup_logging, get_logger
from core.state_manager import TaskStatus
from crews import (
    run_strategy_crew,
    run_curriculum_crew,
    run_platform_crew,
    run_qa_crew
)

console = Console()


def initialize_system():
    """Initialize the system: validate config, create directories, etc."""
    console.print("\n[bold cyan]Initializing AI Mastery Platform System...[/bold cyan]\n")

    # Ensure directories exist
    Config.ensure_directories()
    console.print("✓ Created necessary directories")

    # Validate API keys
    try:
        Config.validate_api_keys()
        console.print("✓ API keys validated")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        console.print("\nPlease set one of the following environment variables:")
        console.print("  - OPENAI_API_KEY")
        console.print("  - ANTHROPIC_API_KEY")
        console.print("\nYou can also create a .env file in the project root.")
        sys.exit(1)

    # Initialize state manager and LLM client
    state_manager = StateManager()
    llm_client = LLMClient()

    console.print("✓ Initialized state manager and LLM client")
    console.print()

    return state_manager, llm_client


def print_phase_header(phase_num: int, phase_name: str):
    """Print a formatted phase header."""
    console.print(
        Panel(
            f"[bold white]Phase {phase_num}: {phase_name}[/bold white]",
            style="bold blue",
            expand=False
        )
    )


def print_crew_result(result: dict):
    """Print the result of a crew execution."""
    if result["status"] == "success":
        console.print(f"[green]✓[/green] {result['crew_name']} completed successfully")
    else:
        console.print(f"[red]✗[/red] {result['crew_name']} failed: {result.get('error', 'Unknown error')}")


def run_all_phases(state_manager: StateManager, llm_client: LLMClient):
    """Run all phases sequentially."""
    logger = setup_logging("main")
    logger.info("Starting full platform development process")

    console.print(
        Panel.fit(
            "[bold cyan]AI Mastery Platform Development System[/bold cyan]\n"
            "Orchestrating multi-agent crews to design your learning platform",
            border_style="cyan"
        )
    )
    console.print()

    # Phase 1: Vision & Requirements
    print_phase_header(1, "Vision & Requirements")
    console.print("Running Strategy Crew (Chief of Staff + Product Manager)...\n")
    result = run_strategy_crew(state_manager, llm_client)
    print_crew_result(result)
    console.print()

    if result["status"] != "success":
        console.print("[bold red]Phase 1 failed. Stopping execution.[/bold red]")
        return

    # Phase 2: Curriculum Construction
    print_phase_header(2, "Curriculum Construction")
    console.print("Running Curriculum Crew (Learning R&D Division)...\n")
    result = run_curriculum_crew(state_manager, llm_client)
    print_crew_result(result)
    console.print()

    if result["status"] != "success":
        console.print("[bold yellow]Phase 2 failed. Continuing with caution...[/bold yellow]")

    # Phase 3: Product & Platform Build
    print_phase_header(3, "Product & Platform Build")
    console.print("Running Platform Crew (Engineering Division)...\n")
    result = run_platform_crew(state_manager, llm_client)
    print_crew_result(result)
    console.print()

    if result["status"] != "success":
        console.print("[bold yellow]Phase 3 failed. Continuing with caution...[/bold yellow]")

    # Phase 4: Testing & Refinement
    print_phase_header(4, "Testing & Refinement")
    console.print("Running QA Crew (QA Researcher)...\n")
    result = run_qa_crew(state_manager, llm_client)
    print_crew_result(result)
    console.print()

    # Final summary
    console.print("\n")
    console.print(
        Panel.fit(
            "[bold green]All phases completed![/bold green]\n"
            "Check the artifacts/ directory for all generated documents.",
            border_style="green"
        )
    )

    # Print cost summary
    print_cost_summary(llm_client)


def print_cost_summary(llm_client: LLMClient):
    """Print LLM usage and cost summary."""
    summary = llm_client.get_session_summary()

    console.print("\n[bold cyan]LLM Usage Summary[/bold cyan]")
    console.print(f"Total API Calls: {summary['total_calls']}")
    console.print(f"Total Tokens: {summary['total_tokens']:,}")
    console.print(f"[bold]Total Cost: ${summary['total_cost']:.4f}[/bold]")

    if summary['by_agent']:
        console.print("\n[bold]Cost by Agent:[/bold]")
        table = Table()
        table.add_column("Agent", style="cyan")
        table.add_column("Calls", justify="right")
        table.add_column("Tokens", justify="right")
        table.add_column("Cost", justify="right", style="yellow")

        for agent, stats in sorted(summary['by_agent'].items(), key=lambda x: x[1]['cost'], reverse=True):
            table.add_row(
                agent,
                str(stats['calls']),
                f"{stats['input_tokens'] + stats['output_tokens']:,}",
                f"${stats['cost']:.4f}"
            )

        console.print(table)


def print_status(state_manager: StateManager):
    """Print current system status."""
    summary = state_manager.get_summary()

    console.print("\n[bold cyan]System Status[/bold cyan]\n")

    # Phase status
    if summary['phases']:
        console.print("[bold]Phase Progress:[/bold]")
        for phase in summary['phases']:
            status_color = {
                'completed': 'green',
                'in_progress': 'yellow',
                'failed': 'red',
                'pending': 'white'
            }.get(phase['status'], 'white')

            console.print(f"  Phase {phase['phase_number']}: {phase['phase_name']} - [{status_color}]{phase['status']}[/{status_color}]")
        console.print()

    # Task counts
    if summary['task_counts']:
        console.print("[bold]Task Summary:[/bold]")
        for status, count in summary['task_counts'].items():
            console.print(f"  {status}: {count}")
        console.print()

    # Artifacts
    artifacts_dir = Config.ARTIFACTS_DIR
    if artifacts_dir.exists():
        artifacts = list(artifacts_dir.glob("*.md"))
        if artifacts:
            console.print(f"[bold]Generated Artifacts ({len(artifacts)}):[/bold]")
            for artifact in sorted(artifacts):
                console.print(f"  - {artifact.name}")


@click.group()
def cli():
    """AI Mastery Platform - Multi-Agent Development System"""
    pass


@cli.command()
def run():
    """Run all phases of the platform development process."""
    state_manager, llm_client = initialize_system()
    run_all_phases(state_manager, llm_client)


@cli.command()
@click.argument('phase', type=click.IntRange(1, 4))
def run_phase(phase: int):
    """Run a specific phase (1-4)."""
    state_manager, llm_client = initialize_system()

    phase_crews = {
        1: ("Vision & Requirements", run_strategy_crew),
        2: ("Curriculum Construction", run_curriculum_crew),
        3: ("Product & Platform Build", run_platform_crew),
        4: ("Testing & Refinement", run_qa_crew)
    }

    phase_name, crew_func = phase_crews[phase]
    print_phase_header(phase, phase_name)

    result = crew_func(state_manager, llm_client)
    print_crew_result(result)

    print_cost_summary(llm_client)


@cli.command()
def status():
    """Show current system status and progress."""
    Config.ensure_directories()
    state_manager = StateManager()
    print_status(state_manager)


@cli.command()
@click.option('--output', '-o', type=click.Path(), help='Output file for the report')
def cost_report(output):
    """Generate a detailed cost analysis report."""
    Config.ensure_directories()
    llm_client = LLMClient()

    output_path = Path(output) if output else None
    report = llm_client.generate_cost_report(output_path)

    console.print(report)

    if output_path:
        console.print(f"\n[green]Report saved to {output_path}[/green]")


@cli.command()
def artifacts():
    """List all generated artifacts."""
    Config.ensure_directories()
    artifacts_dir = Config.ARTIFACTS_DIR

    console.print(f"\n[bold cyan]Generated Artifacts[/bold cyan]")
    console.print(f"Location: {artifacts_dir}\n")

    artifacts = list(artifacts_dir.glob("*.md"))

    if not artifacts:
        console.print("[yellow]No artifacts generated yet.[/yellow]")
        console.print("Run 'python main.py run' to start the development process.")
        return

    table = Table()
    table.add_column("Artifact", style="cyan")
    table.add_column("Size", justify="right")
    table.add_column("Modified", style="dim")

    for artifact in sorted(artifacts):
        stats = artifact.stat()
        size_kb = stats.st_size / 1024
        from datetime import datetime
        modified = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        table.add_row(
            artifact.name,
            f"{size_kb:.1f} KB",
            modified
        )

    console.print(table)


if __name__ == "__main__":
    cli()
