"""User profile collection for personalized AI learning path."""

from typing import Dict


def ask(question: str) -> str:
    """
    Ask a question and get user input.

    Args:
        question: The question to ask

    Returns:
        User's response
    """
    print("\n" + question)
    return input("> ").strip()


def get_user_profile() -> Dict[str, str]:
    """
    Collect user profile information for personalized learning path.

    Returns:
        Dictionary containing user profile data
    """
    print("\n" + "=" * 60)
    print("AI MASTERY PLATFORM - PERSONALIZED LEARNING PATH")
    print("=" * 60)
    print("\nWe'll ask you a few questions to personalize your learning journey.")
    print("Answer freely. Short or long answers are fine.\n")

    profile = {}

    profile["python_skill"] = ask(
        "How would you describe your current Python skill level?"
        "\n(Numbers or words both fine - e.g., 'beginner', 'intermediate', '7/10')"
    )

    profile["ai_experience"] = ask(
        "Have you used any AI tools, libraries, or platforms before?"
        "\nIf yes, describe which ones and how."
        "\n(e.g., 'Used scikit-learn for a project', 'Built a chatbot with OpenAI API', or 'No experience')"
    )

    profile["target_role"] = ask(
        "What specific AI-related role do you want to reach?"
        "\nExamples: Machine Learning Engineer, Data Scientist, AI Architect, AI Tech Lead"
        "\nInclude any career motivation or reason if you'd like."
    )

    profile["industry"] = ask(
        "Which industry are you currently working in (or planning to work in)?"
        "\n(e.g., 'Tech/SaaS', 'Healthcare', 'Finance', 'Education', 'Career switcher - not sure yet')"
    )

    profile["company_alignment"] = ask(
        "Do you want your learning path to be aligned with real company problems or projects?"
        "\nDescribe briefly what kind of problems interest you."
    )

    profile["hardware"] = ask(
        "What computer hardware do you have available? (CPU/GPU specs if known)"
        "\nExamples: 'Mac M1', 'Windows + RTX 3060', 'Just a laptop, not sure', 'Cloud only'"
    )

    profile["budget"] = ask(
        "Do you have a budget for AI tools, compute, or cloud services?"
        "\nIf yes, give a rough monthly or total limit."
        "\n(e.g., '$50/month', 'No budget - free tier only', 'Up to $200 total')"
    )

    profile["time_available"] = ask(
        "How much time can you dedicate to learning? (daily/weekly estimate)"
        "\n(e.g., '1 hour daily', '10 hours/week', 'Full-time for 3 months')"
    )

    profile["weekends"] = ask(
        "Are weekends available for learning or do you prefer rest?"
        "\nDescribe realistically."
        "\n(e.g., 'Yes, can do 4-5 hours Saturday', 'Prefer weekends off', 'Flexible')"
    )

    profile["focus_area"] = ask(
        "Which area of AI feels most interesting or relevant right now?"
        "\nExamples: NLP/LLMs, AI Agents, Computer Vision, MLOps, Training models, RAG systems"
        "\n(or 'Not sure yet - want broad exposure')"
    )

    profile["portfolio_preference"] = ask(
        "Are you open to building a public portfolio (GitHub, blog, open-source),"
        "\nor do you prefer to keep your work private?"
        "\n(e.g., 'Yes, want to build public portfolio', 'Private for now', 'Mix of both')"
    )

    profile["language_preference"] = ask(
        "Are English-language resources okay, or do you prefer another language?"
        "\n(e.g., 'English is fine', 'Prefer Spanish when available', 'Bilingual - both work')"
    )

    print("\n" + "=" * 60)
    print("PROFILE COLLECTED - Thank you!")
    print("=" * 60)
    print("\nYour personalized learning path will be designed based on:")
    print(f"  - Target Role: {profile['target_role']}")
    print(f"  - Focus Area: {profile['focus_area']}")
    print(f"  - Time Available: {profile['time_available']}")
    print(f"  - Current Level: Python {profile['python_skill']}")
    print()

    return profile


def format_profile_for_agents(profile: Dict[str, str]) -> str:
    """
    Format user profile for inclusion in agent prompts.

    Args:
        profile: User profile dictionary

    Returns:
        Formatted string for agent context
    """
    return f"""
USER PROFILE & CONTEXT:

Target Role: {profile.get('target_role', 'Not specified')}
Industry Focus: {profile.get('industry', 'Not specified')}
AI Focus Area: {profile.get('focus_area', 'Not specified')}

Current Skills:
- Python Level: {profile.get('python_skill', 'Not specified')}
- AI Experience: {profile.get('ai_experience', 'No prior experience')}

Learning Constraints:
- Time Available: {profile.get('time_available', 'Not specified')}
- Weekend Availability: {profile.get('weekends', 'Not specified')}
- Hardware: {profile.get('hardware', 'Not specified')}
- Budget: {profile.get('budget', 'Not specified')}

Preferences:
- Company Alignment: {profile.get('company_alignment', 'Not specified')}
- Portfolio: {profile.get('portfolio_preference', 'Not specified')}
- Language: {profile.get('language_preference', 'English')}

IMPORTANT: Design the learning path specifically for THIS user's context, constraints, and goals.
Personalize content difficulty, project suggestions, and time estimates based on their profile.
"""
