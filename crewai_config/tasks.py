"""
Elite Software Development Crew - Task Definitions
===================================================
This module defines all tasks for the development workflow.
"""

from crewai import Task
from textwrap import dedent
from typing import List, Optional


def create_product_requirements_task(agent, context: Optional[List[Task]] = None) -> Task:
    """Phase 1: Product Requirements Definition"""
    return Task(
        description=dedent("""
            Analyze the project brief and create a comprehensive Product Requirements Document (PRD).

            You must:
            1. Understand the core problem being solved and user needs
            2. Define clear, measurable success metrics (KPIs)
            3. Break down features into detailed user stories with acceptance criteria
            4. Prioritize features (Must-have, Should-have, Could-have, Won't-have)
            5. Identify risks, dependencies, and assumptions
            6. Define what is explicitly OUT of scope
            7. Create a phased rollout plan if the project is complex

            Output: Complete PRD including:
            - Executive summary
            - Problem statement and user personas
            - Success metrics and KPIs
            - Detailed user stories with acceptance criteria
            - Feature prioritization matrix (MoSCoW)
            - Risk assessment and mitigation strategies
            - Dependencies and assumptions
            - Out of scope items

            Success Criteria:
            - All features have measurable acceptance criteria
            - Success metrics are specific and measurable
            - Priorities are clear and justified
            - Risks are identified with mitigation plans
        """),
        expected_output="A comprehensive Product Requirements Document (PRD) in markdown format with all sections completed",
        agent=agent,
        context=context or [],
        output_file="output/docs/PRD.md"
    )


def create_system_architecture_task(agent, context: List[Task]) -> Task:
    """Phase 1: System Architecture Design"""
    return Task(
        description=dedent("""
            Design the complete system architecture based on the approved PRD.

            Stack requirements:
            - Frontend: Next.js (App Router, React Server Components)
            - Backend: Node.js (API routes, server actions)
            - ORM: Prisma
            - Database: PostgreSQL (local development)
            - Authentication: NextAuth.js
            - Testing: Jest + Playwright

            You must:
            1. Design the overall system architecture using clean architecture principles
            2. Create detailed database schema with proper normalization and indexes
            3. Define API endpoints and contracts
            4. Design authentication and authorization flows
            5. Establish folder structure following Next.js best practices
            6. Create Architecture Decision Records (ADRs) for key decisions
            7. Define security measures (input validation, CSRF, XSS prevention, etc.)
            8. Establish error handling and logging strategies
            9. Define coding standards and conventions

            Output: Complete architecture documentation including:
            - System architecture diagrams (C4 model)
            - Database schema (ERD) with tables, relationships, constraints, indexes
            - API endpoint specifications
            - Security architecture and threat model
            - Folder structure with detailed rationale
            - Architecture Decision Records (ADRs)
            - Coding standards document
            - Error handling strategy
            - Prisma schema draft

            Success Criteria:
            - Architecture follows SOLID principles and clean architecture
            - Database schema is properly normalized (3NF minimum)
            - Security measures address OWASP Top 10
            - All major decisions are documented in ADRs
        """),
        expected_output="Complete system architecture documentation including diagrams, database schema, API specs, and ADRs",
        agent=agent,
        context=context,
        output_file="output/docs/ARCHITECTURE.md"
    )


def create_uiux_design_task(agent, context: List[Task]) -> Task:
    """Phase 2: UI/UX Design"""
    return Task(
        description=dedent("""
            Create a comprehensive design system and user experience specification.

            You must:
            1. Map out complete user flows for all features from PRD
            2. Create wireframes for all major screens and interactions
            3. Define design system with tokens (colors, typography, spacing, shadows)
            4. Specify component library structure aligned with architecture
            5. Ensure WCAG 2.1 AA accessibility compliance
            6. Define responsive breakpoints and mobile-first approach
            7. Document interaction patterns, animations, and micro-interactions
            8. Create component usage guidelines

            Output: Complete design specification including:
            - User flows and journey maps (mermaid diagrams)
            - Wireframes for all major screens
            - Design tokens specification
            - Component library structure
            - Accessibility guidelines (WCAG 2.1 AA compliance checklist)
            - Responsive design strategy
            - Interaction patterns and animation guidelines
            - Component documentation template

            Success Criteria:
            - All user flows map to user stories from PRD
            - Design system is comprehensive and reusable
            - Accessibility standards are clearly defined
            - Components align with frontend folder structure
        """),
        expected_output="Complete design system specification with user flows, wireframes, design tokens, and component guidelines",
        agent=agent,
        context=context,
        output_file="output/docs/DESIGN_SYSTEM.md"
    )


def create_backend_implementation_task(agent, context: List[Task]) -> Task:
    """Phase 3: Backend Implementation"""
    return Task(
        description=dedent("""
            Implement the complete backend system including database, APIs, and authentication.

            You must:
            1. Implement complete Prisma schema from architecture specification
            2. Create database migrations with proper indexes and constraints
            3. Build all API routes with proper validation (Zod)
            4. Implement NextAuth.js authentication with secure session management
            5. Create authorization middleware and role-based access control
            6. Implement business logic with proper separation of concerns
            7. Add comprehensive error handling and logging
            8. Write integration tests for all API endpoints
            9. Optimize database queries and add necessary indexes
            10. Document all API endpoints with request/response examples

            Technology requirements:
            - Use Prisma for all database operations
            - Use Zod for validation schemas
            - Follow REST API conventions
            - Implement proper HTTP status codes
            - Use environment variables for configuration

            Output: Complete backend implementation including:
            - prisma/schema.prisma (complete schema)
            - prisma/migrations/ (all migrations)
            - app/api/ routes with proper validation
            - lib/auth/ NextAuth configuration
            - lib/db/ database utilities
            - middleware/ for authentication and error handling
            - types/ for TypeScript definitions
            - Integration tests for all endpoints
            - API documentation with examples

            Success Criteria:
            - All database tables match ERD from architecture
            - All API endpoints have validation and error handling
            - Authentication and authorization work correctly
            - Integration tests have >80% coverage
            - No SQL injection or security vulnerabilities
        """),
        expected_output="Complete backend implementation with Prisma schema, API routes, authentication, tests, and documentation",
        agent=agent,
        context=context,
        output_file="output/docs/API_DOCUMENTATION.md"
    )


def create_frontend_implementation_task(agent, context: List[Task]) -> Task:
    """Phase 4: Frontend Implementation"""
    return Task(
        description=dedent("""
            Implement the complete frontend application using Next.js App Router.

            You must:
            1. Set up Next.js project structure following architecture
            2. Implement all pages using App Router conventions
            3. Build reusable components following design system
            4. Implement proper server/client component split
            5. Create custom hooks for business logic
            6. Integrate with backend APIs
            7. Implement form handling with validation
            8. Add loading states, error boundaries, and Suspense
            9. Ensure accessibility (semantic HTML, ARIA, keyboard nav)
            10. Implement responsive design (mobile-first)
            11. Optimize performance (code splitting, lazy loading)
            12. Write unit tests for components and hooks
            13. Add TypeScript types for all props and state

            Technology requirements:
            - Next.js 14+ with App Router
            - React Server Components where appropriate
            - TypeScript for type safety
            - Tailwind CSS or CSS Modules for styling
            - React Hook Form for forms

            Output: Complete frontend implementation including:
            - app/ directory with all pages and layouts
            - components/ with reusable UI components
            - hooks/ with custom React hooks
            - lib/ with utilities and API clients
            - types/ with TypeScript definitions
            - styles/ or Tailwind configuration
            - Component tests
            - Component documentation

            Success Criteria:
            - All pages and components match design specs
            - Accessibility score >95 (Lighthouse)
            - Performance score >90 (Lighthouse)
            - All forms have proper validation
            - Unit tests have >80% coverage
        """),
        expected_output="Complete frontend implementation with pages, components, hooks, tests, and documentation",
        agent=agent,
        context=context,
        output_file="output/docs/COMPONENTS.md"
    )


def create_devops_setup_task(agent, context: List[Task]) -> Task:
    """Phase 5: DevOps & Automation"""
    return Task(
        description=dedent("""
            Set up development environment, automation, and CI/CD pipeline.

            You must:
            1. Create Docker Compose setup for local development (PostgreSQL)
            2. Set up environment variable management (.env.example)
            3. Configure package.json scripts for common tasks
            4. Set up ESLint and Prettier with proper configurations
            5. Configure pre-commit hooks with Husky and lint-staged
            6. Create database seed scripts for development data
            7. Set up CI/CD pipeline (GitHub Actions)
            8. Configure test automation and coverage reporting
            9. Create development onboarding scripts
            10. Set up build optimization and production configuration

            Output: Development environment and automation including:
            - docker-compose.yml
            - Environment configuration files
            - Linting and formatting configs
            - Pre-commit hooks
            - CI/CD pipeline configuration
            - NPM scripts for all common tasks
            - Database seed scripts
            - Developer onboarding documentation

            Success Criteria:
            - One-command setup for new developers
            - All code passes linting and formatting checks
            - Pre-commit hooks catch issues before commit
            - CI pipeline runs tests and builds successfully
        """),
        expected_output="Complete development environment setup with Docker, automation scripts, and CI/CD configuration",
        agent=agent,
        context=context,
        output_file="output/docs/SETUP.md"
    )


def create_qa_testing_task(agent, context: List[Task]) -> Task:
    """Phase 6: Quality Assurance"""
    return Task(
        description=dedent("""
            Perform comprehensive testing, accessibility audits, and performance optimization.

            You must:
            1. Review and enhance existing unit and integration tests
            2. Create comprehensive E2E test suite using Playwright
            3. Test all user flows from design specification
            4. Perform accessibility audit (WCAG 2.1 AA compliance)
            5. Run Lighthouse performance audits
            6. Test error handling and edge cases
            7. Validate security measures (OWASP Top 10 checklist)
            8. Test responsive design across devices
            9. Generate test coverage reports
            10. Create comprehensive bug reports with reproduction steps
            11. Validate all acceptance criteria from PRD

            Testing requirements:
            - Unit tests: >80% coverage (Jest)
            - Integration tests: All API endpoints
            - E2E tests: All critical user flows (Playwright)
            - Accessibility: WCAG 2.1 AA compliance
            - Performance: Lighthouse score >90
            - Security: OWASP Top 10 checklist

            Output: Comprehensive test suite and quality reports including:
            - Enhanced unit tests
            - Integration test suite
            - E2E test suite (Playwright)
            - Accessibility audit report
            - Performance audit report
            - Security audit checklist
            - Test coverage reports
            - Bug reports with severity and reproduction steps

            Success Criteria:
            - All critical user flows have E2E tests
            - Test coverage >80% for business logic
            - Accessibility score >95
            - Performance score >90
            - All OWASP Top 10 vulnerabilities checked
        """),
        expected_output="Complete test suite with coverage reports, accessibility audit, performance audit, and bug reports",
        agent=agent,
        context=context,
        output_file="output/docs/QA_REPORT.md"
    )


def create_backend_refinement_task(agent, context: List[Task]) -> Task:
    """Phase 7: Backend Refinement"""
    return Task(
        description=dedent("""
            Address all backend-related issues identified in QA testing.

            You must:
            1. Review all backend-related bugs from QA report
            2. Fix security vulnerabilities with highest priority
            3. Optimize slow database queries
            4. Improve error handling and validation
            5. Address any API inconsistencies
            6. Update integration tests to cover edge cases
            7. Refactor code smells identified in review
            8. Ensure all fixes have corresponding tests

            Output: Refined backend with:
            - All critical and high-priority bugs fixed
            - Performance optimizations implemented
            - Enhanced error handling
            - Updated tests covering fixes
            - Documentation updates for API changes

            Success Criteria:
            - Zero critical or high-severity bugs
            - All performance recommendations implemented
            - Test coverage maintained or improved
        """),
        expected_output="Refined backend implementation with all QA issues resolved and tests updated",
        agent=agent,
        context=context,
        output_file="output/docs/BACKEND_REFINEMENT.md"
    )


def create_frontend_refinement_task(agent, context: List[Task]) -> Task:
    """Phase 7: Frontend Refinement"""
    return Task(
        description=dedent("""
            Address all frontend-related issues identified in QA testing.

            You must:
            1. Review all frontend-related bugs from QA report
            2. Fix accessibility issues with highest priority
            3. Implement performance optimizations
            4. Improve error boundaries and loading states
            5. Refine responsive design issues
            6. Enhance user feedback mechanisms
            7. Update component tests to cover edge cases
            8. Refactor code smells identified in review
            9. Ensure all fixes maintain design consistency

            Output: Refined frontend with:
            - All critical and high-priority bugs fixed
            - Accessibility issues resolved (WCAG 2.1 AA)
            - Performance optimizations implemented
            - Enhanced user experience
            - Updated tests covering fixes
            - Documentation updates

            Success Criteria:
            - Zero critical or high-severity bugs
            - Accessibility score >95
            - Performance score >90
            - All design specs matched
        """),
        expected_output="Refined frontend implementation with all QA issues resolved and tests updated",
        agent=agent,
        context=context,
        output_file="output/docs/FRONTEND_REFINEMENT.md"
    )


def create_comprehensive_documentation_task(agent, context: List[Task]) -> Task:
    """Phase 8: Documentation"""
    return Task(
        description=dedent("""
            Create complete, production-ready documentation for the entire project.

            You must:
            1. Create comprehensive README with project overview
            2. Document development environment setup (SETUP.md)
            3. Create detailed API documentation with examples
            4. Document all components with usage examples
            5. Write architecture documentation with diagrams
            6. Create deployment guide for production
            7. Write troubleshooting guide for common issues
            8. Create CONTRIBUTING.md for new developers
            9. Maintain CHANGELOG.md with all changes
            10. Add inline code comments for complex logic
            11. Create runbook for operations and maintenance

            Output: Complete documentation suite including:
            - README.md (project overview, features, quick start)
            - SETUP.md (detailed environment setup)
            - ARCHITECTURE.md (system design, decisions)
            - API.md (complete API documentation)
            - COMPONENTS.md (component library with usage)
            - DEPLOYMENT.md (production deployment guide)
            - TROUBLESHOOTING.md (common issues)
            - CONTRIBUTING.md (how to contribute)
            - CHANGELOG.md (version history)
            - RUNBOOK.md (operations and maintenance)

            Success Criteria:
            - New developer can set up environment in <30 minutes
            - All APIs documented with examples
            - All components documented with code examples
            - Troubleshooting covers all common issues
        """),
        expected_output="Complete documentation suite enabling team handoff and long-term maintenance",
        agent=agent,
        context=context,
        output_file="output/docs/README.md"
    )


def create_final_quality_review_task(agent, context: List[Task]) -> Task:
    """Phase 9: Final Review & Sign-off"""
    return Task(
        description=dedent("""
            Perform comprehensive final review and provide production readiness sign-off.

            As Technical Lead, you must:
            1. Review all code for quality, security, and maintainability
            2. Verify adherence to architecture decisions and ADRs
            3. Validate all acceptance criteria from PRD are met
            4. Check security best practices (OWASP Top 10)
            5. Review test coverage and quality
            6. Validate performance and accessibility standards
            7. Ensure documentation is complete and accurate
            8. Check for code smells and technical debt
            9. Verify deployment readiness
            10. Provide detailed feedback for any issues
            11. Sign off on production readiness or request revisions

            Review checklist:
            - Code Quality: Clean code, SOLID principles, DRY
            - Architecture: Follows approved architecture
            - Security: No vulnerabilities, proper auth/authz
            - Performance: Optimized queries, fast load times
            - Testing: Comprehensive coverage, quality tests
            - Accessibility: WCAG 2.1 AA compliance
            - Documentation: Complete, accurate, useful
            - Maintainability: Clear code, good naming
            - Production Readiness: Error handling, logging

            Output: Final quality review report including:
            - Code review summary with findings
            - Architecture compliance assessment
            - Security audit results
            - Performance evaluation
            - Test coverage analysis
            - Documentation completeness check
            - Technical debt assessment
            - Production readiness checklist
            - Specific improvement recommendations (if any)
            - Final approval OR detailed revision requests
            - Sign-off statement

            Success Criteria:
            - All critical issues identified and documented
            - Clear guidance provided for any required changes
            - Production readiness decision is well-justified
        """),
        expected_output="Comprehensive quality review report with production readiness assessment and sign-off",
        agent=agent,
        context=context,
        output_file="output/docs/FINAL_REVIEW.md"
    )


def create_all_tasks(agents: dict) -> List[Task]:
    """
    Create all tasks in the proper order with dependencies.

    Args:
        agents: Dict of agent instances

    Returns:
        List of Task instances in execution order
    """
    # Phase 1: Discovery & Planning
    task_prd = create_product_requirements_task(agents["product_strategist"])

    task_architecture = create_system_architecture_task(
        agents["system_architect"],
        context=[task_prd]
    )

    # Phase 2: Design
    task_design = create_uiux_design_task(
        agents["uiux_designer"],
        context=[task_prd, task_architecture]
    )

    # Phase 3: Backend Implementation
    task_backend = create_backend_implementation_task(
        agents["backend_engineer"],
        context=[task_architecture]
    )

    # Phase 4: Frontend Implementation
    task_frontend = create_frontend_implementation_task(
        agents["frontend_engineer"],
        context=[task_design, task_backend]
    )

    # Phase 5: DevOps
    task_devops = create_devops_setup_task(
        agents["devops_engineer"],
        context=[task_frontend, task_backend]
    )

    # Phase 6: QA
    task_qa = create_qa_testing_task(
        agents["qa_engineer"],
        context=[task_frontend, task_backend, task_devops]
    )

    # Phase 7: Refinement
    task_backend_refinement = create_backend_refinement_task(
        agents["backend_engineer"],
        context=[task_qa]
    )

    task_frontend_refinement = create_frontend_refinement_task(
        agents["frontend_engineer"],
        context=[task_qa]
    )

    # Phase 8: Documentation
    task_docs = create_comprehensive_documentation_task(
        agents["documentation_specialist"],
        context=[task_frontend_refinement, task_backend_refinement, task_devops]
    )

    # Phase 9: Final Review
    task_review = create_final_quality_review_task(
        agents["tech_lead_reviewer"],
        context=[task_docs, task_frontend_refinement, task_backend_refinement, task_qa]
    )

    return [
        task_prd,
        task_architecture,
        task_design,
        task_backend,
        task_frontend,
        task_devops,
        task_qa,
        task_backend_refinement,
        task_frontend_refinement,
        task_docs,
        task_review,
    ]
