# Elite Software Development Crew

A fully-configured CrewAI system that operates like a top 1% professional software development company, building high-quality web applications from requirements to production-ready code.

## Overview

This CrewAI configuration creates a team of 9 specialized AI agents that work together to build complete web applications following industry best practices. The crew handles everything from product strategy to final quality review.

### Tech Stack

The crew builds applications using:

- **Frontend**: Next.js 14+ (App Router, React Server Components)
- **Backend**: Node.js (API Routes, Server Actions)
- **Database**: PostgreSQL (local development)
- **ORM**: Prisma
- **Authentication**: NextAuth.js
- **Testing**: Jest + Playwright
- **Styling**: Tailwind CSS / CSS Modules
- **Environment**: Docker + Docker Compose

## Agents

The crew consists of 9 specialized agents:

### 1. Product Strategist AI
- Defines feature requirements and success metrics
- Creates Product Requirements Documents (PRDs)
- Establishes user stories with acceptance criteria
- **Tools**: Analysis, Markdown Generation

### 2. System Architect AI
- Designs system architecture and database schema
- Creates Architecture Decision Records (ADRs)
- Establishes security and coding standards
- **Tools**: Analysis, Markdown Generation, PostgreSQL Query, Filesystem Writer

### 3. UI/UX Designer AI
- Creates design systems and component libraries
- Ensures WCAG 2.1 AA accessibility compliance
- Designs user flows and wireframes
- **Tools**: Analysis, Markdown Generation, Filesystem Writer

### 4. Backend Engineer AI
- Implements Prisma schemas and migrations
- Builds secure API endpoints with validation
- Implements authentication and authorization
- **Tools**: Filesystem Writer, Process Executor, PostgreSQL Query, Jest Runner, Git

### 5. Frontend Engineer AI
- Implements Next.js pages and components
- Ensures accessibility and performance
- Integrates with backend APIs
- **Tools**: Filesystem Writer, Process Executor, Jest Runner, Playwright Runner, Git

### 6. DevOps Engineer AI
- Creates Docker development environment
- Sets up CI/CD pipelines
- Configures linting, formatting, and pre-commit hooks
- **Tools**: Filesystem Writer, Process Executor, Docker CLI, Git

### 7. QA & Performance Auditor AI
- Writes comprehensive test suites
- Performs accessibility and performance audits
- Validates security measures (OWASP Top 10)
- **Tools**: Jest Runner, Playwright Runner, Process Executor, Analysis, Markdown Generation

### 8. Documentation Specialist AI
- Creates comprehensive documentation
- Writes setup guides and API documentation
- Maintains changelogs and contributing guides
- **Tools**: Markdown Generation, Filesystem Writer, Analysis

### 9. Technical Lead & Reviewer AI
- Performs final quality review
- Ensures adherence to best practices
- Provides production readiness sign-off
- **Tools**: Analysis, Process Executor, Git, Markdown Generation

## Workflow

The crew follows a sequential 9-phase workflow:

### Phase 1: Discovery & Planning
1. **Product Requirements** - PRD with user stories and acceptance criteria
2. **System Architecture** - Architecture design, database schema, ADRs

### Phase 2: Design
3. **UI/UX Design** - Design system, wireframes, component library structure

### Phase 3: Backend Implementation
4. **Backend Development** - Prisma schema, API routes, authentication, tests

### Phase 4: Frontend Implementation
5. **Frontend Development** - Pages, components, hooks, integration, tests

### Phase 5: DevOps & Automation
6. **DevOps Setup** - Docker, CI/CD, linting, automation scripts

### Phase 6: Quality Assurance
7. **QA Testing** - Comprehensive testing, accessibility audit, performance audit

### Phase 7: Bug Fixes & Refinement
8. **Backend Refinement** - Fix issues identified in QA
9. **Frontend Refinement** - Fix issues identified in QA

### Phase 8: Documentation
10. **Comprehensive Documentation** - Complete docs suite

### Phase 9: Final Review
11. **Quality Review & Sign-off** - Final review and production readiness assessment

## Quality Standards

All deliverables must meet:

- **Code Quality**: SOLID principles, clean architecture, DRY
- **Security**: OWASP Top 10 compliance, no critical vulnerabilities
- **Testing**: >80% test coverage
- **Accessibility**: WCAG 2.1 AA compliance (Lighthouse score >95)
- **Performance**: Lighthouse performance score >90
- **Documentation**: Complete and accurate

## Installation

### Prerequisites

- Python 3.10 or higher
- Node.js 18+ and npm (for running generated projects)
- Docker and Docker Compose (optional, for generated projects)
- OpenAI API key

### Setup

1. **Clone or navigate to the crew configuration directory:**

```bash
cd crewai_config
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the Crew

**Option 1: Use the default project brief**

```bash
python main.py
```

This runs the crew with a default task management application project.

**Option 2: Provide a custom project brief**

Create a text file with your project requirements:

```bash
# my_project.txt
Build a blog platform with user authentication, post creation,
comments, and markdown support. Must be mobile-responsive and
accessible.
```

Run the crew with your brief:

```bash
python main.py my_project.txt
```

### Output Structure

All generated files are created in the `output/` directory:

```
output/
├── docs/                      # All documentation
│   ├── README.md             # Project overview
│   ├── PRD.md                # Product requirements
│   ├── ARCHITECTURE.md       # System architecture
│   ├── DESIGN_SYSTEM.md      # UI/UX specifications
│   ├── API_DOCUMENTATION.md  # API reference
│   ├── COMPONENTS.md         # Component library
│   ├── SETUP.md              # Development setup
│   ├── QA_REPORT.md          # Quality assurance results
│   ├── FINAL_REVIEW.md       # Production readiness review
│   └── ...
├── app/                      # Next.js app directory
├── components/               # React components
├── lib/                      # Utilities and helpers
├── prisma/                   # Database schema and migrations
├── tests/                    # Test files
├── scripts/                  # Automation scripts
├── public/                   # Static assets
└── .github/                  # CI/CD workflows
```

### Next Steps After Generation

1. **Review the output:**
   ```bash
   cd output
   cat docs/README.md
   ```

2. **Set up the generated project:**
   ```bash
   # Follow instructions in docs/SETUP.md
   npm install
   docker-compose up -d
   npx prisma migrate dev
   npm run dev
   ```

3. **Review quality reports:**
   - `docs/QA_REPORT.md` - Testing and quality metrics
   - `docs/FINAL_REVIEW.md` - Production readiness assessment

## Configuration

### Main Configuration

The crew behavior is configured in [crew_config.yaml](crew_config.yaml):

- Process type (sequential)
- Quality gates and thresholds
- Technology stack specifications
- Success criteria
- Collaboration rules

### Agent Configuration

Agent definitions are in [agents.yaml](agents.yaml):

- Roles and responsibilities
- Personas and expertise
- Tool assignments
- Output format expectations

### Task Configuration

Task workflow is defined in [tasks.yaml](tasks.yaml):

- Task descriptions and requirements
- Input/output specifications
- Success criteria
- Dependencies and execution order

## Customization

### Changing the Tech Stack

Edit `crew_config.yaml` to modify the technology stack:

```yaml
tech_stack:
  frontend:
    framework: "Next.js 14+"
    styling: "Tailwind CSS / CSS Modules"  # Change this
  backend:
    orm: "Prisma"  # Change to another ORM if needed
```

### Adjusting Quality Thresholds

Modify quality gates in `crew_config.yaml`:

```yaml
quality_gates:
  - name: "test_coverage"
    threshold: 80  # Change threshold
  - name: "accessibility_score"
    threshold: 95  # Change threshold
```

### Adding Custom Agents

1. Add agent definition to `agents.yaml`
2. Create agent function in `agents.py`
3. Assign appropriate tools
4. Create tasks for the agent in `tasks.py`
5. Add to workflow in `crew_config.yaml`

### Modifying the Workflow

Edit `tasks.py` to change task order or dependencies:

```python
# Change task context to modify dependencies
task_frontend = create_frontend_implementation_task(
    agents["frontend_engineer"],
    context=[task_design, task_backend]  # Modify dependencies
)
```

## Tools Available

The crew has access to these tools:

- **Filesystem Writer** - Create/update files
- **Filesystem Reader** - Read existing files
- **Directory Tools** - Navigate and search directories
- **Local Process Executor** - Run npm, node, prisma, tests
- **PostgreSQL Query** - Validate database schema
- **Docker CLI** - Manage containers
- **Git Tool** - Version control operations
- **Jest Runner** - Unit and integration tests
- **Playwright Runner** - End-to-end tests
- **Markdown Generator** - Create documentation
- **Analysis Tool** - Self-critique and validation
- **Web Search** - Research best practices

## Best Practices

### Writing Effective Project Briefs

Include:

1. **Core Features** - What the application should do
2. **User Roles** - Who will use it and their permissions
3. **Technical Requirements** - Performance, accessibility, security
4. **Success Metrics** - How to measure success
5. **Constraints** - Budget, timeline, technology limitations (if any)

### Example Project Brief

```
Build an e-commerce platform with the following:

Core Features:
- Product catalog with search and filters
- Shopping cart and checkout
- User accounts and order history
- Admin dashboard for inventory management
- Payment processing integration

User Roles:
- Customer: Browse, purchase, view orders
- Admin: Manage products, view analytics

Technical Requirements:
- Mobile-responsive design
- Fast page loads (<2s)
- Secure payment processing
- WCAG 2.1 AA accessible
- SEO-friendly

Success Metrics:
- Lighthouse performance >90
- Accessibility score >95
- Zero critical security issues
- Test coverage >80%
```

## Troubleshooting

### Common Issues

**Issue: OpenAI API rate limits**

Solution: The crew uses GPT-4 by default. If you hit rate limits:
- Use GPT-3.5-turbo for faster, cheaper processing
- Edit `main.py` and change `llm_model="gpt-3.5-turbo"`

**Issue: Memory errors with large projects**

Solution:
- Break project into phases
- Run specific phases separately
- Increase context window by using GPT-4-turbo

**Issue: Generated code has errors**

Solution:
- Check `docs/QA_REPORT.md` for known issues
- Review `docs/FINAL_REVIEW.md` for improvement recommendations
- Re-run specific tasks with refined requirements

### Getting Help

1. Check the generated `docs/TROUBLESHOOTING.md` in output
2. Review task outputs in `docs/` for detailed reports
3. Check agent logs for specific error messages

## Advanced Usage

### Running Specific Phases Only

Modify `main.py` to run only certain tasks:

```python
# In create_all_tasks(), comment out tasks you don't need
tasks = [
    task_prd,
    task_architecture,
    # task_design,        # Skip design phase
    # task_backend,       # Skip backend
    # ...
]
```

### Using Different LLMs

The crew uses OpenAI by default but can be configured for other LLMs:

```python
# In main.py, change the LLM initialization
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-opus-20240229")
```

### Parallel Task Execution

For independent tasks (like backend and frontend refinement), modify process type:

```python
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    process=Process.hierarchical,  # Allows parallel execution
    manager_llm=llm
)
```

## Architecture

### System Design

The crew follows a **sequential process** where each agent completes their work before passing to the next. This ensures:

- Clear handoffs between specialists
- Complete deliverables at each stage
- Quality validation before proceeding
- Comprehensive documentation trail

### Tool Architecture

Tools are modular and can be assigned to any agent:

```python
# In tools.py
class CustomTool:
    name = "Custom Tool"
    description = "What this tool does"

    @staticmethod
    def run(params):
        # Tool implementation
        pass
```

### Memory and Context

The crew uses CrewAI's memory system to:

- Retain context between tasks
- Reference previous decisions
- Maintain consistency across phases
- Enable agents to build on prior work

## Performance Considerations

### Execution Time

A complete workflow typically takes:

- **Small projects** (< 5 features): 15-30 minutes
- **Medium projects** (5-15 features): 30-60 minutes
- **Large projects** (15+ features): 1-3 hours

Factors affecting time:
- Number of features
- Complexity of requirements
- LLM model used (GPT-4 vs GPT-3.5)
- Number of refinement iterations

### Cost Estimation

Using GPT-4:
- **Small projects**: $5-15
- **Medium projects**: $15-40
- **Large projects**: $40-100+

Using GPT-3.5-turbo can reduce costs by 90%.

## Contributing

To improve or extend this crew:

1. **Add new agents** in `agents.yaml` and `agents.py`
2. **Create new tasks** in `tasks.yaml` and `tasks.py`
3. **Build custom tools** in `tools.py`
4. **Adjust quality standards** in `crew_config.yaml`
5. **Enhance workflows** in `main.py`

## License

This configuration is provided as-is for educational and commercial use.

## Credits

Built with [CrewAI](https://www.crewai.com/) - AI agent orchestration framework.

---

**Ready to build?** Run `python main.py` to start creating production-ready web applications!
