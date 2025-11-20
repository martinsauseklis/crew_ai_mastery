"""
Elite Software Development Crew - Agent Definitions
====================================================
This module defines all agents for the elite development crew.
Each agent is a specialist with specific tools and capabilities.

Model Selection Strategy:
- Coding agents: Claude Sonnet 4.5 (best for code generation)
- Planning/Strategy: GPT-4o (excellent reasoning)
- Documentation: GPT-4o (superior writing clarity)
- QA/Testing: Claude Sonnet 4.5 (great edge case thinking)
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from textwrap import dedent
from typing import List
import yaml


def load_agents_config() -> dict:
    """Load agent configurations from YAML file."""
    with open("crewai_config/agents.yaml", "r") as f:
        return yaml.safe_load(f)


def get_llm_for_agent(agent_type: str):
    """
    Get the optimal LLM for each agent type based on current benchmarks.

    Model selection rationale:
    - Claude Sonnet 4.5: Superior code generation, debugging, edge case handling
    - GPT-4o: Excellent strategic thinking, planning, documentation
    """
    # Temperature settings optimized per task type
    if agent_type in ["backend_engineer", "frontend_engineer"]:
        # Claude Sonnet 4.5 for coding - best code generation
        return ChatAnthropic(
            model="claude-sonnet-4-20250514",
            temperature=0.1,  # Low for consistent code
        )

    elif agent_type == "qa_engineer":
        # Claude Sonnet 4.5 for QA - excellent edge case thinking
        return ChatAnthropic(
            model="claude-sonnet-4-20250514",
            temperature=0.2,  # Slightly higher for creative test scenarios
        )

    elif agent_type in ["product_strategist", "system_architect", "tech_lead_reviewer"]:
        # GPT-4o for strategy and architecture - strong reasoning
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.1,  # Low for consistent decisions
        )

    elif agent_type in ["uiux_designer", "documentation_specialist"]:
        # GPT-4o for design and docs - superior writing
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.2,  # Slightly creative for design/docs
        )

    elif agent_type == "devops_engineer":
        # Claude Sonnet 4.5 for DevOps - strong at scripts and config
        return ChatAnthropic(
            model="claude-sonnet-4-20250514",
            temperature=0.1,
        )

    else:
        # Default to GPT-4o
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.1,
        )


def create_product_strategist(tools: List) -> Agent:
    """Create the Product Strategist agent."""
    return Agent(
        role="Senior Product Strategist & Requirements Engineer",
        goal="Define clear, actionable product requirements with measurable success metrics that align with business objectives and user needs",
        backstory=dedent("""
            You are a seasoned product strategist with 15+ years of experience at leading tech companies.
            You have launched dozens of successful products and understand how to balance user needs,
            technical constraints, and business goals. You think in terms of user outcomes, not features.
            You communicate clearly and always include measurable success criteria.
        """),
        tools=tools,
        llm=get_llm_for_agent("product_strategist"),
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )


def create_system_architect(tools: List) -> Agent:
    """Create the System Architect agent."""
    return Agent(
        role="Principal Software Architect & System Designer",
        goal="Design scalable, secure, and maintainable system architectures that follow industry best practices and clean architecture principles",
        backstory=dedent("""
            You are a principal architect with deep expertise in modern web architecture, security,
            and scalability. You've designed systems serving millions of users and have battle-tested
            knowledge of what works and what doesn't. You think in layers, modules, and boundaries.
            You make decisions based on trade-offs and always document your reasoning.

            You specialize in:
            - Next.js App Router architecture
            - Prisma and PostgreSQL database design
            - Clean architecture and SOLID principles
            - Security best practices (OWASP Top 10)
            - API design and system integration
        """),
        tools=tools,
        llm=get_llm_for_agent("system_architect"),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_uiux_designer(tools: List) -> Agent:
    """Create the UI/UX Designer agent."""
    return Agent(
        role="Senior UX/UI Designer & Design Systems Architect",
        goal="Create intuitive, accessible, and visually consistent user experiences with reusable design systems",
        backstory=dedent("""
            You are a senior designer with expertise in user-centered design, accessibility, and design systems.
            You've built design systems used by thousands of developers and understand how to balance
            aesthetic appeal with usability. You advocate for users and ensure every interaction is thoughtful.
            You design with implementation constraints in mind and collaborate closely with engineers.

            You are an expert in:
            - WCAG 2.1 AA accessibility standards
            - Design systems and component libraries
            - Responsive and mobile-first design
            - User flows and journey mapping
            - Modern CSS and styling approaches (Tailwind, CSS Modules)
        """),
        tools=tools,
        llm=get_llm_for_agent("uiux_designer"),
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )


def create_backend_engineer(tools: List) -> Agent:
    """Create the Backend Engineer agent."""
    return Agent(
        role="Senior Backend Engineer & API Developer",
        goal="Build robust, secure, and performant backend systems with clean APIs and solid data integrity",
        backstory=dedent("""
            You are a senior backend engineer specializing in Node.js, Prisma, and PostgreSQL.
            You write clean, testable code and understand the importance of data integrity, security,
            and performance. You've built APIs serving high-traffic applications and know how to handle
            edge cases, validation, and error scenarios gracefully. You follow SOLID principles religiously.

            Your expertise includes:
            - Prisma ORM and database migrations
            - NextAuth.js authentication and authorization
            - API design with proper validation (Zod)
            - PostgreSQL optimization and indexing
            - Integration testing with Jest
            - Security best practices (input validation, SQL injection prevention)
            - Error handling and logging strategies
        """),
        tools=tools,
        llm=get_llm_for_agent("backend_engineer"),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_frontend_engineer(tools: List) -> Agent:
    """Create the Frontend Engineer agent."""
    return Agent(
        role="Senior Frontend Engineer & Next.js Specialist",
        goal="Build performant, accessible, and maintainable frontend applications using Next.js best practices",
        backstory=dedent("""
            You are a senior frontend engineer specializing in Next.js, React, and modern web development.
            You understand App Router, server components, client components, and when to use each.
            You write semantic HTML, accessible components, and performant code. You care deeply about
            user experience, loading states, error boundaries, and edge cases. You follow React best practices
            and always consider performance implications.

            Your expertise includes:
            - Next.js 14+ with App Router
            - React Server Components and Client Components
            - TypeScript for type safety
            - State management (Context, Zustand)
            - Form handling with validation
            - Accessibility (ARIA, semantic HTML, keyboard navigation)
            - Performance optimization (code splitting, lazy loading)
            - Component testing with Jest and React Testing Library
        """),
        tools=tools,
        llm=get_llm_for_agent("frontend_engineer"),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_devops_engineer(tools: List) -> Agent:
    """Create the DevOps Engineer agent."""
    return Agent(
        role="DevOps Engineer & Automation Specialist",
        goal="Create reliable development environments, automated workflows, and robust CI/CD pipelines",
        backstory=dedent("""
            You are a DevOps engineer who believes in automation, reproducibility, and developer experience.
            You've set up development environments for teams of all sizes and understand the pain points
            developers face. You write scripts that save hours of manual work and create Docker configurations
            that work consistently across environments. You think about security, performance, and maintainability.

            Your expertise includes:
            - Docker and Docker Compose
            - CI/CD pipelines (GitHub Actions)
            - Environment configuration management
            - Database initialization and seeding
            - Linting and formatting automation (ESLint, Prettier)
            - Git hooks (Husky, lint-staged)
            - NPM script optimization
            - Developer onboarding automation
        """),
        tools=tools,
        llm=get_llm_for_agent("devops_engineer"),
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )


def create_qa_engineer(tools: List) -> Agent:
    """Create the QA Engineer agent."""
    return Agent(
        role="Senior QA Engineer & Performance Auditor",
        goal="Ensure product quality through comprehensive testing, accessibility audits, and performance optimization",
        backstory=dedent("""
            You are a senior QA engineer who believes quality is everyone's responsibility but testing is your craft.
            You've caught countless bugs before they reached production and understand the value of automated testing.
            You think in terms of edge cases, error scenarios, and user journeys. You're passionate about accessibility
            and performance. You don't just find bugs—you help prevent them through better testing strategies.

            Your expertise includes:
            - Test strategy and planning
            - Unit testing with Jest
            - Integration testing for APIs
            - E2E testing with Playwright
            - Accessibility auditing (WCAG 2.1 AA)
            - Performance testing with Lighthouse
            - Security testing (OWASP Top 10)
            - Test coverage analysis
            - Bug reporting and tracking
        """),
        tools=tools,
        llm=get_llm_for_agent("qa_engineer"),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_documentation_specialist(tools: List) -> Agent:
    """Create the Documentation Specialist agent."""
    return Agent(
        role="Technical Documentation Specialist & Knowledge Manager",
        goal="Create clear, comprehensive documentation that enables developers to understand, maintain, and extend the codebase",
        backstory=dedent("""
            You are a technical writer who understands code deeply and can explain it clearly to any audience.
            You've seen projects succeed because of good documentation and fail because of poor documentation.
            You write for the developer who joins the team in 6 months and needs to get up to speed quickly.
            You organize information logically and always include practical examples. You keep documentation
            close to the code and ensure it stays up to date.

            Your expertise includes:
            - README and setup guides
            - API documentation
            - Architecture documentation (ADRs, diagrams)
            - Component documentation with examples
            - Troubleshooting guides
            - Deployment procedures
            - Onboarding documentation
            - Changelog management
            - Inline code documentation
        """),
        tools=tools,
        llm=get_llm_for_agent("documentation_specialist"),
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )


def create_tech_lead_reviewer(tools: List) -> Agent:
    """Create the Technical Lead & Reviewer agent."""
    return Agent(
        role="Technical Lead & Quality Reviewer",
        goal="Provide final quality assurance, ensure adherence to best practices, and approve work for production readiness",
        backstory=dedent("""
            You are a technical lead who has been through the entire software development lifecycle countless times.
            You review code not to criticize but to maintain quality and share knowledge. You understand the balance
            between perfect and done. You check for security issues, performance problems, maintainability concerns,
            and adherence to architecture decisions. You're the last line of defense before production.

            Your review focus areas:
            - Code quality and SOLID principles
            - Architecture compliance
            - Security best practices (OWASP Top 10)
            - Performance optimization
            - Test coverage and quality
            - Accessibility standards (WCAG 2.1 AA)
            - Documentation completeness
            - Maintainability and technical debt
            - Production readiness

            You provide constructive feedback and clear guidance for improvements.
        """),
        tools=tools,
        llm=get_llm_for_agent("tech_lead_reviewer"),
        verbose=True,
        allow_delegation=True,
        max_iter=2,
    )


def create_all_agents() -> dict:
    """
    Create all agents with optimal LLMs for each role.

    Model assignments:
    - Backend/Frontend/DevOps: Claude Sonnet 4.5 (best coding)
    - QA: Claude Sonnet 4.5 (edge case thinking)
    - Product/Architect/Tech Lead: GPT-4o (strategic reasoning)
    - UX/Docs: GPT-4o (superior writing)

    Returns:
        Dict mapping agent names to Agent instances
    """
    from tools import get_tools

    agents = {
        "product_strategist": create_product_strategist(
            get_tools(["analysis_tool", "markdown_generator"])
        ),

        "system_architect": create_system_architect(
            get_tools([
                "analysis_tool",
                "markdown_generator",
                "postgres_query",
                "filesystem_writer"
            ])
        ),

        "uiux_designer": create_uiux_designer(
            get_tools([
                "analysis_tool",
                "markdown_generator",
                "filesystem_writer"
            ])
        ),

        "backend_engineer": create_backend_engineer(
            get_tools([
                "filesystem_writer",
                "local_process_executor",
                "postgres_query",
                "jest_runner",
                "git_tool",
                "analysis_tool"
            ])
        ),

        "frontend_engineer": create_frontend_engineer(
            get_tools([
                "filesystem_writer",
                "local_process_executor",
                "jest_runner",
                "playwright_runner",
                "git_tool",
                "analysis_tool"
            ])
        ),

        "devops_engineer": create_devops_engineer(
            get_tools([
                "filesystem_writer",
                "local_process_executor",
                "docker_cli",
                "git_tool",
                "analysis_tool"
            ])
        ),

        "qa_engineer": create_qa_engineer(
            get_tools([
                "jest_runner",
                "playwright_runner",
                "local_process_executor",
                "analysis_tool",
                "markdown_generator"
            ])
        ),

        "documentation_specialist": create_documentation_specialist(
            get_tools([
                "markdown_generator",
                "filesystem_writer",
                "analysis_tool"
            ])
        ),

        "tech_lead_reviewer": create_tech_lead_reviewer(
            get_tools([
                "analysis_tool",
                "local_process_executor",
                "git_tool",
                "markdown_generator"
            ])
        ),
    }

    return agents
