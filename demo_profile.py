"""Quick user profile collection for demo mode (2-3 questions)."""

from typing import Dict
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def get_demo_user_profile() -> Dict[str, str]:
    """
    Collect quick user profile for demo (2-3 questions only).

    Returns:
        Dictionary containing user profile data
    """
    console.print()
    console.print(Panel.fit(
        "[bold cyan]AI MASTERY PLATFORM - DEMO MODE[/bold cyan]\n"
        "[dim]Quick Profile Setup (3 questions)[/dim]",
        border_style="cyan"
    ))
    console.print()

    profile = {}

    # Question 1: Experience level
    console.print("[bold]1. What's your current AI/ML experience level?[/bold]")
    experience = Prompt.ask(
        "   Choose",
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate"
    )
    profile["ai_experience"] = experience
    profile["python_skill"] = experience  # Assume similar levels

    # Question 2: Primary goal
    console.print("\n[bold]2. What's your primary learning goal?[/bold]")
    goal = Prompt.ask(
        "   Choose",
        choices=["career-change", "skill-enhancement", "academic", "hobby"],
        default="skill-enhancement"
    )
    profile["target_role"] = {
        "career-change": "Machine Learning Engineer (career switch)",
        "skill-enhancement": "Senior ML Engineer / AI Tech Lead",
        "academic": "AI Researcher / PhD candidate",
        "hobby": "AI Enthusiast / Side Projects"
    }[goal]

    # Question 3: Time commitment
    console.print("\n[bold]3. How much time can you dedicate weekly?[/bold]")
    time = Prompt.ask(
        "   Choose",
        choices=["1-5hrs", "5-10hrs", "10-20hrs", "20+hrs"],
        default="5-10hrs"
    )
    profile["time_available"] = {
        "1-5hrs": "1-5 hours per week",
        "5-10hrs": "5-10 hours per week",
        "10-20hrs": "10-20 hours per week (evenings + weekends)",
        "20+hrs": "20+ hours per week (nearly full-time)"
    }[time]

    # Set sensible defaults for other fields used by agents
    profile["industry"] = "Technology/Software"
    profile["focus_area"] = "LLMs and AI Agents" if experience != "beginner" else "AI/ML Fundamentals"
    profile["hardware"] = "Standard laptop (cloud-first approach)"
    profile["budget"] = "$50-100/month for cloud services and APIs"
    profile["weekends"] = "Available for learning"
    profile["company_alignment"] = "Yes, real-world projects preferred"
    profile["portfolio_preference"] = "Public portfolio on GitHub"
    profile["language_preference"] = "English"

    console.print()
    console.print(Panel(
        f"[bold green]✓ Profile Created[/bold green]\n\n"
        f"[dim]Experience:[/dim] {experience.capitalize()}\n"
        f"[dim]Goal:[/dim] {profile['target_role']}\n"
        f"[dim]Time:[/dim] {profile['time_available']}",
        border_style="green"
    ))

    return profile


def format_demo_profile_for_agents(profile: Dict[str, str]) -> str:
    """
    Format demo user profile for inclusion in agent prompts.

    Args:
        profile: User profile dictionary

    Returns:
        Formatted string for agent context
    """
    return f"""
USER PROFILE & CONTEXT (DEMO):

Target Role: {profile.get('target_role', 'Not specified')}
AI Focus Area: {profile.get('focus_area', 'Not specified')}

Current Skills:
- AI Experience Level: {profile.get('ai_experience', 'intermediate')}
- Python Level: {profile.get('python_skill', 'intermediate')}

Learning Constraints:
- Time Available: {profile.get('time_available', '5-10 hours per week')}
- Hardware: {profile.get('hardware', 'Standard laptop')}
- Budget: {profile.get('budget', '$50-100/month')}

IMPORTANT: Design the learning path specifically for THIS user's context.
This is a DEMO - keep outputs concise (300-500 words) while showing the key insights.
"""
