# Elite Software Development Crew - Quick Reference

## ⚡ Quick Start Commands

```bash
# Setup
cd crewai_config
pip install -r requirements.txt
cp .env.example .env
# Edit .env: Add OPENAI_API_KEY

# Run in INTERACTIVE mode (answer prompts)
python main.py

# Or use a requirements FILE
python main.py my_project.txt

# Use GPT-3.5 for cost savings
python main.py my_project.txt --model gpt-3.5-turbo

# Test generated project
cd output
npm install
docker-compose up -d
npx prisma migrate dev
npm test
npm run dev
```

## 📁 File Structure

```
crewai_config/
├── agents.yaml          # Agent definitions
├── tasks.yaml           # Task definitions
├── crew_config.yaml     # Main configuration
├── tools.py             # Tool implementations
├── agents.py            # Agent creation
├── tasks.py             # Task creation
├── main.py              # Orchestration
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── README.md            # Documentation
├── USAGE_GUIDE.md       # Detailed guide
├── SUMMARY.md           # Complete summary
├── WORKFLOW_DIAGRAM.md  # Visual workflow
└── QUICK_REFERENCE.md   # This file
```

## 🤖 Agents at a Glance

| # | Agent | Experience | Key Tools | Primary Output |
|---|-------|-----------|-----------|----------------|
| 1 | Product Strategist | 15+ years | Analysis, Markdown | PRD.md |
| 2 | System Architect | 20+ years | Analysis, Markdown, PostgreSQL, Filesystem | ARCHITECTURE.md |
| 3 | UI/UX Designer | 12+ years | Analysis, Markdown, Filesystem | DESIGN_SYSTEM.md |
| 4 | Backend Engineer | 10+ years | Filesystem, Process, PostgreSQL, Jest, Git | Backend code + API docs |
| 5 | Frontend Engineer | 10+ years | Filesystem, Process, Jest, Playwright, Git | Frontend code + components |
| 6 | DevOps Engineer | 8+ years | Filesystem, Process, Docker, Git | DevOps setup + configs |
| 7 | QA Engineer | 12+ years | Jest, Playwright, Process, Analysis | QA_REPORT.md |
| 8 | Documentation Specialist | 10+ years | Markdown, Filesystem, Analysis | Complete docs/ |
| 9 | Tech Lead Reviewer | 20+ years | Analysis, Process, Git, Markdown | FINAL_REVIEW.md |

## 🔄 Workflow Phases

1. **Discovery & Planning** → PRD + Architecture
2. **Design** → Design System
3. **Backend** → APIs + Database
4. **Frontend** → Pages + Components
5. **DevOps** → Environment + CI/CD
6. **QA** → Tests + Audits
7. **Refinement** → Bug Fixes
8. **Documentation** → Complete Docs
9. **Review** → Final Sign-off

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend Framework | Next.js 14+ (App Router) |
| Frontend Language | TypeScript |
| Styling | Tailwind CSS / CSS Modules |
| State Management | React Context / Zustand |
| Backend Runtime | Node.js |
| Backend Framework | Next.js API Routes |
| Database | PostgreSQL |
| ORM | Prisma |
| Authentication | NextAuth.js |
| Validation | Zod |
| Unit Testing | Jest |
| Component Testing | React Testing Library |
| E2E Testing | Playwright |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Linting | ESLint |
| Formatting | Prettier |
| Git Hooks | Husky + lint-staged |

## ✅ Quality Gates

| Gate | Requirement | Threshold |
|------|------------|-----------|
| Security | No critical vulnerabilities | Required |
| Test Coverage | Unit + Integration tests | >80% |
| Accessibility | WCAG 2.1 AA compliance | Score >95 |
| Performance | Lighthouse performance | Score >90 |
| Documentation | All docs complete | Required |

## 📊 Output Directory Structure

```
output/
├── docs/                      # Documentation
│   ├── README.md
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── DESIGN_SYSTEM.md
│   ├── API_DOCUMENTATION.md
│   ├── COMPONENTS.md
│   ├── SETUP.md
│   ├── QA_REPORT.md
│   ├── FINAL_REVIEW.md
│   └── ...
├── app/                       # Next.js app
├── components/                # React components
├── lib/                       # Utilities
├── prisma/                    # Database
├── tests/                     # Tests
├── scripts/                   # Automation
├── public/                    # Static assets
├── .github/                   # CI/CD
├── docker-compose.yml
├── package.json
└── ...
```

## 🔧 Available Tools

1. **Filesystem Writer** - Create/update files
2. **Filesystem Reader** - Read files
3. **Directory Reader** - List directories
4. **Directory Search** - Search directories
5. **Code Docs Search** - Search documentation
6. **Local Process Executor** - Run commands
7. **PostgreSQL Query** - Database queries
8. **Docker CLI** - Docker commands
9. **Git Tool** - Version control
10. **Jest Runner** - Unit tests
11. **Playwright Runner** - E2E tests
12. **Markdown Generator** - Generate docs
13. **Analysis Tool** - Self-critique
14. **Web Search** - Research

## 💡 Common Customizations

### Change LLM Model

```python
# In main.py
result = run_crew(project_brief, llm_model="gpt-3.5-turbo")
```

### Adjust Quality Thresholds

```yaml
# In crew_config.yaml
quality_gates:
  - name: "test_coverage"
    threshold: 90  # Change from 80
```

### Change Tech Stack

```yaml
# In crew_config.yaml
tech_stack:
  frontend:
    styling: "Styled Components"  # Change from Tailwind
```

### Skip Phases

```python
# In main.py, create_all_tasks()
tasks = [
    task_prd,
    task_architecture,
    # task_design,  # Skip this
    task_backend,
    # ...
]
```

## 🎯 Project Brief Template

```
[PROJECT NAME]

## Overview
Brief description

## Core Features
- Feature 1
- Feature 2
- ...

## User Roles
- Role 1: Permissions
- Role 2: Permissions

## Technical Requirements
- Performance: < 2s load time
- Accessibility: WCAG 2.1 AA
- Security: No critical issues

## Success Metrics
- Lighthouse performance >90
- Lighthouse accessibility >95
- Test coverage >80%
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Rate limits | Use GPT-3.5-turbo |
| Long execution | Reduce scope or skip phases |
| Code errors | Check QA_REPORT.md |
| Missing files | Verify task completion |
| Test failures | Check environment setup |

## 📈 Performance

| Project Size | Time | Cost (GPT-4) | Cost (GPT-3.5) |
|-------------|------|--------------|----------------|
| Small (< 5 features) | 15-30 min | $5-15 | $0.50-1.50 |
| Medium (5-15 features) | 30-60 min | $15-40 | $1.50-4.00 |
| Large (15+ features) | 1-3 hours | $40-100+ | $4.00-10.00 |

## 🎨 Agent Responsibilities Summary

**Product Strategist**: Requirements, user stories, success metrics

**System Architect**: Architecture, database, security, ADRs

**UI/UX Designer**: Design system, wireframes, accessibility

**Backend Engineer**: APIs, database, auth, tests

**Frontend Engineer**: Pages, components, integration, tests

**DevOps Engineer**: Docker, CI/CD, automation

**QA Engineer**: Testing, audits, bug reports

**Documentation Specialist**: All documentation

**Tech Lead Reviewer**: Final review, sign-off

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| [README.md](README.md) | Overview & installation |
| [USAGE_GUIDE.md](USAGE_GUIDE.md) | Detailed usage instructions |
| [SUMMARY.md](SUMMARY.md) | Complete summary |
| [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md) | Visual workflow |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | This file |
| [agents.yaml](agents.yaml) | Agent definitions |
| [tasks.yaml](tasks.yaml) | Task definitions |
| [crew_config.yaml](crew_config.yaml) | Main config |

## 🔐 Environment Variables

```bash
# Required
OPENAI_API_KEY=your_key_here

# Optional
DATABASE_URL=postgresql://user:pass@localhost:5432/db
SERPER_API_KEY=your_serper_key_here
LLM_MODEL=gpt-4
EMBEDDING_MODEL=text-embedding-3-small
OUTPUT_DIR=output
```

## ⚙️ Configuration Files

| File | Purpose |
|------|---------|
| `.env` | Environment variables |
| `agents.yaml` | Agent definitions |
| `tasks.yaml` | Task workflow |
| `crew_config.yaml` | Main settings |
| `tools.py` | Tool implementations |
| `agents.py` | Agent factories |
| `tasks.py` | Task factories |
| `main.py` | Entry point |

## 🚀 Best Practices

1. **Start small** - Test with simple project first
2. **Be specific** - Clear requirements = better output
3. **Define metrics** - Include measurable success criteria
4. **Review output** - Check FINAL_REVIEW.md and QA_REPORT.md
5. **Iterate** - Refine based on results
6. **Use version control** - Git commit generated code
7. **Customize** - Adjust for your needs
8. **Document changes** - Update CHANGELOG.md

## 💻 Generated Project Commands

```bash
# After crew completes
cd output

# Install dependencies
npm install

# Start database
docker-compose up -d

# Run migrations
npx prisma migrate dev

# Seed database
npm run seed

# Run tests
npm test

# Run E2E tests
npm run test:e2e

# Lint code
npm run lint

# Format code
npm run format

# Build project
npm run build

# Start development server
npm run dev

# Start production server
npm start
```

## 🔍 Quality Checklist

Before deployment, verify:

- [ ] All tests pass
- [ ] Linting passes
- [ ] Build succeeds
- [ ] Test coverage >80%
- [ ] Accessibility score >95
- [ ] Performance score >90
- [ ] No critical security issues
- [ ] Documentation complete
- [ ] Environment variables documented
- [ ] Database migrations work
- [ ] CI/CD pipeline configured

## 📞 Getting Help

1. Read [README.md](README.md)
2. Check [USAGE_GUIDE.md](USAGE_GUIDE.md)
3. Review `output/docs/TROUBLESHOOTING.md`
4. Check agent logs
5. Review task outputs in `docs/`

## 🎓 Learning Resources

- **CrewAI Docs**: https://docs.crewai.com/
- **Next.js Docs**: https://nextjs.org/docs
- **Prisma Docs**: https://www.prisma.io/docs
- **NextAuth Docs**: https://next-auth.js.org/
- **Playwright Docs**: https://playwright.dev/

## 🏆 Success Criteria

Project is ready when:

- ✅ All quality gates passed
- ✅ Tech lead approved
- ✅ All tests pass
- ✅ Documentation complete
- ✅ No critical issues
- ✅ Performance targets met
- ✅ Accessibility compliant
- ✅ Security validated

---

**Keep this handy for quick reference while working with the Elite Development Crew!** 🚀
