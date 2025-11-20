"""Implementation agents for actually coding the platform."""

from crewai import Agent
from core import LLMClient


def create_implementation_architect(llm_client: LLMClient) -> Agent:
    """
    Create an Implementation Architect agent who plans the coding implementation.

    Returns:
        CrewAI Agent configured for implementation planning
    """
    return Agent(
        role="Implementation Architect",
        goal=(
            "Create a detailed implementation plan for building the AI Mastery Platform, "
            "breaking down the architecture into specific, implementable code files and modules."
        ),
        backstory=(
            "You're a senior software architect who excels at taking high-level designs "
            "and breaking them into concrete, implementable components. You understand both "
            "backend and frontend development, and can create pragmatic implementation plans "
            "that real developers can follow. You prioritize MVP scope and working code over "
            "perfect architecture."
        ),
        llm=llm_client.get_llm(
            model="gpt-4o",
            temperature=0.4,
            agent_name="Implementation Architect"
        ),
        verbose=True,
        allow_delegation=False
    )


def create_backend_implementer(llm_client: LLMClient) -> Agent:
    """
    Create a Backend Implementer agent who writes actual backend code.

    Returns:
        CrewAI Agent configured for backend implementation
    """
    return Agent(
        role="Backend Implementation Developer",
        goal=(
            "Write production-ready backend code for the AI Mastery Platform, including "
            "API endpoints, database models, authentication, and core business logic."
        ),
        backstory=(
            "You're an expert Python backend developer with deep experience in Flask, FastAPI, "
            "SQLAlchemy, and building scalable web applications. You write clean, well-documented "
            "code with proper error handling, validation, and security. You follow best practices "
            "and create code that's maintainable and testable. You excel at implementing RESTful "
            "APIs and database schemas."
        ),
        llm=llm_client.get_llm(
            model="gpt-4o",
            temperature=0.3,
            agent_name="Backend Implementer"
        ),
        verbose=True,
        allow_delegation=False
    )


def create_frontend_implementer(llm_client: LLMClient) -> Agent:
    """
    Create a Frontend Implementer agent who writes actual frontend code.

    Returns:
        CrewAI Agent configured for frontend implementation
    """
    return Agent(
        role="Frontend Implementation Developer",
        goal=(
            "Write production-ready frontend code for the AI Mastery Platform, including "
            "React components, pages, routing, state management, and API integration."
        ),
        backstory=(
            "You're an expert frontend developer with mastery of React, Next.js, TypeScript, "
            "and modern CSS. You write clean, reusable components with proper prop types and "
            "state management. You understand responsive design, accessibility, and performance "
            "optimization. You create beautiful, intuitive user interfaces that match the UX "
            "design specifications."
        ),
        llm=llm_client.get_llm(
            model="gpt-4o",
            temperature=0.3,
            agent_name="Frontend Implementer"
        ),
        verbose=True,
        allow_delegation=False
    )


def create_devops_implementer(llm_client: LLMClient) -> Agent:
    """
    Create a DevOps Implementer agent who creates deployment and setup files.

    Returns:
        CrewAI Agent configured for DevOps implementation
    """
    return Agent(
        role="DevOps Implementation Engineer",
        goal=(
            "Create deployment configurations, Docker files, environment setup, and "
            "documentation to make the AI Mastery Platform easy to run locally and deploy."
        ),
        backstory=(
            "You're a DevOps engineer who excels at making applications easy to run and deploy. "
            "You create clear Docker configurations, setup scripts, environment templates, and "
            "comprehensive README files. You understand both local development setup and cloud "
            "deployment. You write deployment configs that just work."
        ),
        llm=llm_client.get_llm(
            model="gpt-4o",
            temperature=0.3,
            agent_name="DevOps Implementer"
        ),
        verbose=True,
        allow_delegation=False
    )
