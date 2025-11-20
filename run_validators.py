#!/usr/bin/env python3
"""
Run Platform Validators

This script runs validation agents to test the AI Mastery Platform
implementation and generate fixes for any issues found.

Usage:
    python run_validators.py
"""

import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich import box

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.config import Config
from core import StateManager, LLMClient
from demo_config import DemoConfig
from crews.validator_crew import run_validator_crew


console = Console()


def main():
    """Main entry point"""
    try:
        # Print banner
        console.print()
        console.print(Panel.fit(
            "[bold cyan]AI MASTERY PLATFORM[/bold cyan]\n"
            "[bold yellow]VALIDATOR AGENTS[/bold yellow]\n\n"
            "[dim]Automated testing and debugging[/dim]",
            border_style="cyan",
            box=box.DOUBLE
        ))
        console.print()

        console.print("[bold]What will be tested:[/bold]")
        console.print("  • Backend API endpoints and database models")
        console.print("  • Frontend React components and routing")
        console.print("  • End-to-end user flows and integration")
        console.print("  • Demo data alignment with design docs")
        console.print("  • Automated fix generation")
        console.print()

        console.print("[bold]Validators:[/bold]")
        console.print("  1. Backend Validation Engineer (GPT-4o)")
        console.print("  2. Frontend Validation Engineer (GPT-4o)")
        console.print("  3. Integration Test Engineer (Claude Sonnet 4)")
        console.print("  4. Data Quality Engineer (Claude Sonnet 4)")
        console.print("  5. Debug Assistant & Code Fixer (Claude Sonnet 4)")
        console.print()

        console.print("[dim]Estimated time: 5-8 minutes[/dim]")
        console.print("[dim]Estimated cost: $2-4[/dim]")
        console.print()

        # Confirm
        response = console.input("[bold yellow]Start validation? (y/n):[/bold yellow] ")
        if response.lower() != 'y':
            console.print("[yellow]Validation cancelled.[/yellow]")
            return

        # Initialize system
        console.print("\n[bold]Initializing...[/bold]")
        Config.ensure_directories()
        DemoConfig.ensure_demo_directories()
        Config.validate_api_keys()

        state_manager = StateManager()
        llm_client = LLMClient()

        console.print("[green]✓ System initialized[/green]\n")

        # Run validators
        console.print("[bold cyan]Running validation crew...[/bold cyan]\n")
        result = run_validator_crew(state_manager, llm_client)

        if result["status"] == "success":
            console.print("\n[bold green]✓ VALIDATION SUCCESSFUL[/bold green]")
            console.print(f"\nGenerated {result.get('reports_generated', 5)} reports")
        else:
            console.print(f"\n[bold red]✗ VALIDATION FAILED[/bold red]")
            console.print(f"Error: {result.get('error', 'Unknown error')}")
            sys.exit(1)

    except KeyboardInterrupt:
        console.print("\n[yellow]Validation interrupted by user.[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        import traceback
        console.print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
