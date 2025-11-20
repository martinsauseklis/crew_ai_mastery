# Elite Software Development Crew - Usage Guide

Complete guide for using the Elite Software Development Crew to build production-ready web applications.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Understanding the Workflow](#understanding-the-workflow)
3. [Writing Effective Project Briefs](#writing-effective-project-briefs)
4. [Customizing the Crew](#customizing-the-crew)
5. [Advanced Usage](#advanced-usage)
6. [Quality Assurance](#quality-assurance)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Quick Start

### 1. Prerequisites

Ensure you have:
- Python 3.10+
- OpenAI API key
- Node.js 18+ (for running generated projects)
- Docker (optional, for generated projects)

### 2. Installation

```bash
# Navigate to crew directory
cd crewai_config

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 3. Run Your First Project

```bash
# Run with default project brief
python main.py

# Or provide a custom brief
python main.py my_project_brief.txt
```

### 4. Review Output

```bash
cd output
cat docs/README.md      # Project overview
cat docs/SETUP.md       # How to run the project
cat docs/FINAL_REVIEW.md  # Quality assessment
```

---

## Understanding the Workflow

### The 9 Phases

#### Phase 1: Discovery & Planning

**Product Strategist** creates a comprehensive PRD:
- User stories with acceptance criteria
- Success metrics and KPIs
- Feature prioritization
- Risk assessment

**System Architect** designs the system:
- Architecture diagrams
- Database schema
- API specifications
- Security architecture
- ADRs (Architecture Decision Records)

**Output**: `docs/PRD.md`, `docs/ARCHITECTURE.md`

---

#### Phase 2: Design

**UI/UX Designer** creates the design system:
- User flows and wireframes
- Design tokens (colors, typography, spacing)
- Component library structure
- Accessibility guidelines (WCAG 2.1 AA)
- Responsive design strategy

**Output**: `docs/DESIGN_SYSTEM.md`

---

#### Phase 3: Backend Implementation

**Backend Engineer** builds the backend:
- Prisma schema and migrations
- API routes with validation
- Authentication (NextAuth.js)
- Authorization and middleware
- Integration tests
- API documentation

**Output**:
- `prisma/schema.prisma`
- `prisma/migrations/`
- `app/api/`
- `lib/auth/`
- `tests/integration/`
- `docs/API_DOCUMENTATION.md`

---

#### Phase 4: Frontend Implementation

**Frontend Engineer** builds the UI:
- Next.js pages and layouts
- Reusable React components
- Custom hooks
- API integration
- Form handling and validation
- Accessibility implementation
- Component tests

**Output**:
- `app/` (pages and layouts)
- `components/`
- `hooks/`
- `tests/unit/`
- `docs/COMPONENTS.md`

---

#### Phase 5: DevOps & Automation

**DevOps Engineer** sets up the environment:
- Docker Compose for local dev
- CI/CD pipeline (GitHub Actions)
- ESLint and Prettier configs
- Pre-commit hooks (Husky)
- NPM scripts
- Database seed scripts

**Output**:
- `docker-compose.yml`
- `.github/workflows/`
- `.eslintrc.json`
- `.prettierrc`
- `package.json`
- `docs/SETUP.md`

---

#### Phase 6: Quality Assurance

**QA Engineer** tests everything:
- Unit and integration tests
- E2E tests (Playwright)
- Accessibility audit
- Performance audit (Lighthouse)
- Security validation (OWASP Top 10)
- Bug reports

**Output**:
- `tests/e2e/`
- `docs/QA_REPORT.md`

---

#### Phase 7: Bug Fixes & Refinement

**Backend Engineer** and **Frontend Engineer** fix issues:
- Address bugs from QA report
- Fix security vulnerabilities
- Optimize performance
- Enhance accessibility
- Update tests

**Output**:
- Updated code with fixes
- `docs/BACKEND_REFINEMENT.md`
- `docs/FRONTEND_REFINEMENT.md`

---

#### Phase 8: Documentation

**Documentation Specialist** creates comprehensive docs:
- README with quick start
- Setup guide
- API documentation
- Component documentation
- Troubleshooting guide
- Deployment guide
- Contributing guide
- Changelog

**Output**: Complete `docs/` directory

---

#### Phase 9: Final Review

**Technical Lead** performs final review:
- Code quality assessment
- Architecture compliance
- Security audit
- Performance evaluation
- Test coverage analysis
- Documentation review
- Production readiness checklist
- Sign-off or revision requests

**Output**: `docs/FINAL_REVIEW.md`

---

## Writing Effective Project Briefs

### Structure of a Good Brief

```
[PROJECT NAME]

## Overview
Brief description of what you're building and why.

## Core Features
List of main features:
- Feature 1 with description
- Feature 2 with description
- ...

## User Roles
Who will use the system:
- Role 1: Permissions and capabilities
- Role 2: Permissions and capabilities

## Technical Requirements
- Performance requirements
- Accessibility requirements
- Security requirements
- Browser/device support
- Any specific technology preferences

## Success Metrics
How to measure success:
- Metric 1: Target value
- Metric 2: Target value

## Constraints (Optional)
- Timeline
- Budget
- Technology restrictions
- Integration requirements
```

### Example 1: Simple Blog

```
Personal Blog Platform

## Overview
A modern blog platform for writers to publish articles with markdown support.

## Core Features
- User authentication (email/password)
- Write and publish articles in markdown
- Rich text editor with preview
- Article comments
- Categories and tags
- Article search
- RSS feed

## User Roles
- Author: Create, edit, publish articles
- Reader: Read articles, leave comments
- Admin: Manage users and content

## Technical Requirements
- Mobile-responsive design
- Fast page loads (<2 seconds)
- SEO-friendly (meta tags, sitemap)
- WCAG 2.1 AA accessible
- Support for code syntax highlighting

## Success Metrics
- Lighthouse performance score >90
- Lighthouse accessibility score >95
- Test coverage >80%
- Page load time <2 seconds
```

### Example 2: E-commerce Platform

```
E-commerce Store

## Overview
Full-featured e-commerce platform for selling physical products online.

## Core Features
- Product catalog with categories
- Search with filters (price, category, rating)
- Shopping cart
- Checkout process
- Payment integration (Stripe)
- Order management
- User accounts with order history
- Product reviews and ratings
- Admin dashboard
  - Inventory management
  - Order tracking
  - Sales analytics

## User Roles
- Customer: Browse, purchase, review products
- Admin: Manage products, view orders, analytics
- Warehouse: Update inventory, fulfill orders

## Technical Requirements
- Mobile-first responsive design
- Fast search with debouncing
- Optimistic UI updates for cart
- Secure payment processing (PCI compliance)
- WCAG 2.1 AA accessible
- Support for product images (multiple per product)
- Email notifications for orders

## Success Metrics
- Lighthouse performance >90
- Lighthouse accessibility >95
- Cart-to-purchase conversion >10%
- Zero critical security vulnerabilities
- Test coverage >85%
- Average page load <2 seconds

## Constraints
- Must integrate with existing inventory system API
- Use Stripe for payments
```

### Example 3: SaaS Dashboard

```
Analytics Dashboard SaaS

## Overview
Real-time analytics dashboard for tracking business metrics.

## Core Features
- User authentication with SSO
- Real-time data visualization
  - Line charts for trends
  - Bar charts for comparisons
  - Pie charts for distributions
- Customizable dashboards
- Widget library (drag-and-drop)
- Data export (CSV, PDF)
- Team collaboration
  - Share dashboards
  - Comments on widgets
  - Activity log
- Alerts and notifications
- API for data ingestion
- Webhook integrations

## User Roles
- Viewer: View dashboards
- Editor: Create and edit dashboards
- Admin: Manage users and billing
- API User: Send data via API

## Technical Requirements
- Real-time updates (WebSocket or SSE)
- Handle large datasets (100k+ rows)
- Responsive design (desktop primary, mobile secondary)
- Fast chart rendering (<1 second)
- Dark mode support
- Keyboard navigation for accessibility
- Data refresh every 30 seconds

## Success Metrics
- Initial page load <3 seconds
- Chart render time <1 second
- Lighthouse accessibility >95
- 99.9% uptime
- Test coverage >80%
- API response time <200ms

## Constraints
- Must support PostgreSQL and MongoDB
- Real-time updates required
- Multi-tenant architecture
```

---

## Customizing the Crew

### Changing Quality Thresholds

Edit [crew_config.yaml](crew_config.yaml):

```yaml
quality_gates:
  - name: "test_coverage"
    threshold: 90  # Increase from 80 to 90
    required: true

  - name: "performance_score"
    threshold: 95  # Increase from 90 to 95
    required: true
```

### Modifying Tech Stack

Edit [crew_config.yaml](crew_config.yaml):

```yaml
tech_stack:
  frontend:
    framework: "Next.js 14+"
    styling: "Styled Components"  # Change from Tailwind

  backend:
    orm: "TypeORM"  # Change from Prisma

  testing:
    e2e: "Cypress"  # Change from Playwright
```

### Adding a Custom Agent

1. **Define in agents.yaml:**

```yaml
seo_specialist:
  role: "SEO Specialist & Performance Expert"
  goal: "Optimize application for search engines and performance"
  backstory: "You are an SEO expert..."
  tools:
    - "analysis_tool"
    - "filesystem_writer"
```

2. **Create agent function in agents.py:**

```python
def create_seo_specialist(llm, tools: List) -> Agent:
    return Agent(
        role="SEO Specialist & Performance Expert",
        goal="Optimize application for search engines and performance",
        backstory="You are an SEO expert...",
        tools=tools,
        llm=llm,
        verbose=True,
    )
```

3. **Add to create_all_agents() in agents.py:**

```python
agents = {
    # ... existing agents ...
    "seo_specialist": create_seo_specialist(
        llm,
        get_tools(["analysis_tool", "filesystem_writer"])
    ),
}
```

4. **Create task in tasks.py:**

```python
def create_seo_optimization_task(agent, context: List[Task]) -> Task:
    return Task(
        description="Optimize application for SEO...",
        expected_output="SEO optimization report",
        agent=agent,
        context=context,
    )
```

5. **Add to workflow in tasks.py:**

```python
# In create_all_tasks()
task_seo = create_seo_optimization_task(
    agents["seo_specialist"],
    context=[task_frontend, task_backend]
)
```

---

## Advanced Usage

### Running Specific Phases Only

Modify `main.py` to skip phases:

```python
# In create_all_tasks()
tasks = [
    task_prd,              # Keep
    task_architecture,     # Keep
    # task_design,        # Skip design
    task_backend,          # Keep
    # task_frontend,      # Skip frontend
    # ... etc
]
```

### Using Different LLM Models

**Option 1: Change in main.py**

```python
# Use GPT-3.5 Turbo (faster, cheaper)
result = run_crew(project_brief, llm_model="gpt-3.5-turbo")

# Use GPT-4 Turbo (larger context)
result = run_crew(project_brief, llm_model="gpt-4-turbo-preview")
```

**Option 2: Use different LLM provider**

```python
# In main.py
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    temperature=0.1
)
```

### Adjusting Agent Iterations

In `agents.yaml`:

```yaml
backend_engineer:
  # ...
  max_iterations: 5  # Increase from 3 to 5 for complex tasks
```

Or in `agents.py`:

```python
def create_backend_engineer(llm, tools: List) -> Agent:
    return Agent(
        # ...
        max_iter=5,  # Increase iterations
    )
```

### Custom Tool Creation

Create a new tool in `tools.py`:

```python
class LighthouseAuditTool:
    """Run Lighthouse performance audits."""

    name = "Lighthouse Audit Tool"
    description = "Run Lighthouse performance and accessibility audits"

    @staticmethod
    def run(url: str) -> dict[str, Any]:
        """Run Lighthouse audit on a URL."""
        command = f"lighthouse {url} --output json"
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return {
                "success": True,
                "report": json.loads(result.stdout)
            }
        else:
            return {
                "success": False,
                "error": result.stderr
            }

# Add to ALL_TOOLS
ALL_TOOLS["lighthouse_audit"] = LighthouseAuditTool()
```

Then assign to agents:

```python
"qa_engineer": create_qa_engineer(
    llm,
    get_tools([
        "jest_runner",
        "playwright_runner",
        "lighthouse_audit",  # Add custom tool
        "analysis_tool"
    ])
),
```

---

## Quality Assurance

### Understanding Quality Gates

Quality gates ensure minimum standards are met:

```yaml
quality_gates:
  - name: "security_check"
    description: "No critical security vulnerabilities"
    required: true

  - name: "test_coverage"
    threshold: 80
    required: true
```

**Required gates**: Must pass to continue
**Threshold gates**: Must meet minimum value

### Reviewing Output

After the crew finishes, review these files:

1. **docs/FINAL_REVIEW.md** - Overall quality assessment
2. **docs/QA_REPORT.md** - Detailed test results
3. **docs/ARCHITECTURE.md** - System design decisions

### Testing Generated Code

```bash
cd output

# Install dependencies
npm install

# Start database
docker-compose up -d

# Run migrations
npx prisma migrate dev

# Run tests
npm test

# Run E2E tests
npm run test:e2e

# Start dev server
npm run dev
```

### Quality Checklist

- [ ] All tests pass (`npm test`)
- [ ] E2E tests pass (`npm run test:e2e`)
- [ ] Linting passes (`npm run lint`)
- [ ] Build succeeds (`npm run build`)
- [ ] Test coverage >80%
- [ ] Accessibility score >95
- [ ] Performance score >90
- [ ] No critical security issues
- [ ] Documentation is complete

---

## Troubleshooting

### Issue: Rate Limits

**Problem**: OpenAI API rate limit errors

**Solutions**:
1. Use GPT-3.5-turbo: `python main.py --model gpt-3.5-turbo`
2. Add delays between tasks (modify `main.py`)
3. Upgrade OpenAI API plan

### Issue: Long Execution Time

**Problem**: Crew takes too long to complete

**Solutions**:
1. Use faster model (GPT-3.5-turbo)
2. Reduce scope in project brief
3. Skip non-essential phases
4. Reduce agent iterations in config

### Issue: Generated Code Has Errors

**Problem**: TypeScript errors or build failures

**Solutions**:
1. Check `docs/QA_REPORT.md` for known issues
2. Review `docs/FINAL_REVIEW.md` for recommendations
3. Manually fix remaining issues
4. Re-run specific tasks with corrections

### Issue: Missing Files

**Problem**: Expected files not generated

**Solutions**:
1. Check agent logs for errors
2. Verify task completion in output
3. Check output directory structure
4. Re-run with verbose=True

### Issue: Tests Failing

**Problem**: Generated tests fail

**Solutions**:
1. Review test output for specific failures
2. Check environment setup (DATABASE_URL, etc.)
3. Verify dependencies installed (`npm install`)
4. Check if migrations ran (`npx prisma migrate dev`)

---

## Best Practices

### 1. Start Small

Begin with a simple project to understand the workflow:

```
Simple Todo App

Features:
- Create, read, update, delete todos
- Mark as complete
- Filter by status

This helps you understand output structure and quality.
```

### 2. Be Specific in Requirements

**Bad**: "Build a blog with comments"

**Good**:
```
Build a blog with:
- Markdown editor with live preview
- Draft and published states
- Nested comments (max 3 levels)
- Comment moderation (approve/reject)
- Email notifications for new comments
```

### 3. Define Success Metrics

Always include measurable success criteria:

```
Success Metrics:
- Page load time <2 seconds
- Lighthouse accessibility >95
- Test coverage >85%
- Zero critical security vulnerabilities
```

### 4. Review Before Deploying

Always review:
1. `docs/FINAL_REVIEW.md` - Sign-off status
2. `docs/QA_REPORT.md` - Test results
3. Security checklist in QA report
4. Known issues and limitations

### 5. Iterate on Failures

If quality gates fail:
1. Review failure reasons
2. Refine project brief
3. Adjust quality thresholds if needed
4. Re-run affected phases

### 6. Use Version Control

Commit generated code to git:

```bash
cd output
git init
git add .
git commit -m "Initial generation from Elite Development Crew"
```

### 7. Customize for Your Needs

The crew is a starting point:
- Modify agents for your domain
- Add custom tools
- Adjust quality standards
- Change tech stack

### 8. Document Changes

If you modify generated code:
1. Update `CHANGELOG.md`
2. Add comments explaining changes
3. Update relevant documentation
4. Consider regenerating with updated brief

---

## Example Workflows

### Workflow 1: MVP Development

```bash
# 1. Create brief for MVP
cat > mvp_brief.txt << EOF
Build an MVP task manager with:
- User authentication
- Create/edit/delete tasks
- Mark tasks complete
- Simple dashboard
EOF

# 2. Generate with fast model
python main.py mvp_brief.txt --model gpt-3.5-turbo

# 3. Review output
cd output
cat docs/README.md

# 4. Setup and test
npm install
docker-compose up -d
npx prisma migrate dev
npm test
npm run dev
```

### Workflow 2: Full Production App

```bash
# 1. Create detailed brief
# Include all features, roles, requirements

# 2. Generate with best model
python main.py production_brief.txt --model gpt-4

# 3. Review quality reports
cat output/docs/FINAL_REVIEW.md
cat output/docs/QA_REPORT.md

# 4. Address any issues
# Fix critical items manually

# 5. Re-run QA phase
# Modify main.py to run only QA task

# 6. Final review and deploy
```

### Workflow 3: Learning/Prototyping

```bash
# Generate multiple variations
python main.py brief_v1.txt
mv output output_v1

python main.py brief_v2.txt
mv output output_v2

# Compare approaches
diff -r output_v1 output_v2

# Choose best version
```

---

## Next Steps

After reading this guide:

1. **Try the Quick Start** - Run your first project
2. **Review Generated Output** - Understand what's created
3. **Customize** - Adjust for your needs
4. **Iterate** - Improve based on results
5. **Build** - Create real applications

For more information, see:
- [README.md](README.md) - Overview and installation
- [crew_config.yaml](crew_config.yaml) - Main configuration
- [agents.yaml](agents.yaml) - Agent definitions
- [tasks.yaml](tasks.yaml) - Task workflow

---

**Happy Building!** 🚀
