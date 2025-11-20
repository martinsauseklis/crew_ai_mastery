# AI Mastery Platform - Demo Mode

## Overview

The demo mode provides a **fast, cost-effective way to evaluate the entire AI Mastery Platform** workflow, including all 13 agents, 4 crews, and 17 tasks, with reduced output expectations.

### Demo vs Production

| Aspect | Demo Mode | Production Mode |
|--------|-----------|-----------------|
| **Agents** | All 17 agents (13 + 4 implementation) | All 13 agents |
| **Crews** | All 5 crews (including implementation) | All 4 crews |
| **Tasks** | 21 tasks (17 design + 4 implementation) | 17 tasks (design only) |
| **Models** | Same models (GPT-4o, Claude Sonnet 4.5) | Same models |
| **Output Length** | ~300-500 words per task | ~1000-2500 words per task |
| **Max Iterations** | 5 per agent | 15 per agent |
| **Profile Questions** | 3 quick questions | 11 detailed questions |
| **Implementation** | ✅ YES - Generates actual code | ❌ NO - Design only |
| **Time** | ~15-20 minutes | ~30-60 minutes |
| **Cost** | ~$8-15 | ~$15-30 |
| **Artifacts** | `artifacts/demo/` | `artifacts/` |

## Quick Start

### Prerequisites

1. **Python 3.10+** installed
2. **API Keys** configured in `.env` file:
   ```bash
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

3. **Dependencies** installed:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Demo

Simply run:

```bash
python run_demo.py
```

### What Happens

1. **Welcome Screen**: Overview of what the demo will do
2. **System Initialization**: Validates API keys and creates directories
3. **Quick Profile** (3 questions):
   - Current AI/ML experience level
   - Primary learning goal
   - Weekly time commitment
4. **Agent Overview**: Shows all 17 agents being initialized
5. **Phase 1: Strategy Crew** (~2-3 minutes)
   - Agents: Chief of Staff, Product Manager
   - Tasks: 3 (learning objectives, PRD, roadmap)
6. **Phase 2: Curriculum Crew** (~3-4 minutes)
   - Agents: Curriculum Architect, AI SME, Instructional Designer, Cognitive Scientist, Behavior Designer
   - Tasks: 5 (scaffold, validation, learning science, content, engagement)
7. **Phase 3: Platform Crew** (~4-5 minutes)
   - Agents: UX Designer, Full-Stack Dev, Backend Engineer, ML Engineer, LLM Engineer
   - Tasks: 6 (UX, architecture, data, ML, LLM, MVP plan)
8. **Phase 4: QA Crew** (~2-3 minutes)
   - Agents: QA Researcher
   - Tasks: 3 (review, backlog, validation framework)
9. **Phase 5: Implementation Crew** (~4-5 minutes) **✨ NEW!**
   - Agents: Implementation Architect, Backend Implementer, Frontend Implementer, DevOps Implementer
   - Tasks: 4 (implementation plan, backend code, frontend code, deployment setup)
   - **Generates actual runnable code for the platform!**
10. **Summary Dashboard**: Shows completion status, time, cost, and next steps

### Key Features

- **✅ Ultra-Fast Artifact Skipping**: Checks if artifacts exist BEFORE starting crews (~4ms per phase)
  - If all phase artifacts exist, skips entire phase in <1 second
  - No agent creation, no LLM calls, no API costs
  - Only runs crews for phases with missing artifacts
- **✅ Actual Code Generation**: Phase 5 generates complete, runnable backend and frontend code
- **✅ Smart Extraction**: Only extracts code if platform_code/ doesn't exist yet
- **✅ Same Workflow**: Uses the exact same CrewAI workflow as production (sequential, task dependencies, etc.)

## Demo Outputs

All demo artifacts are saved to `artifacts/demo/`:

### Phase 1 Outputs
- `learning_objectives.md` - Personalized learning objectives
- `prd.md` - Product Requirements Document
- `roadmap.md` - Product roadmap

### Phase 2 Outputs
- `curriculum_scaffold.md` - Curriculum structure
- `technical_validation.md` - Technical depth assessment
- `learning_science_overlay.md` - Cognitive science optimization
- `instructional_content_outline.md` - Lesson plans
- `engagement_systems.md` - Habit formation design

### Phase 3 Outputs
- `ux_design.md` - User experience design
- `system_architecture.md` - Technical architecture
- `data_infrastructure.md` - Database schema
- `ml_systems_design.md` - ML personalization
- `llm_integration_design.md` - LLM tutoring integration
- `mvp_implementation_plan.md` - Development roadmap

### Phase 4 Outputs
- `qa_comprehensive_review.md` - Quality evaluation
- `refinement_backlog.md` - Prioritized improvements
- `validation_framework.md` - Success metrics

### Phase 5 Outputs (Implementation) **✨ NEW!**
- `implementation_plan.md` - Detailed implementation plan with file structure
- `backend_implementation.md` - Complete backend code (Flask/FastAPI app)
- `frontend_implementation.md` - Complete frontend code (React/Next.js)
- `deployment_setup.md` - Docker configs and deployment instructions
- **`platform_code/`** - **ACTUAL RUNNABLE CODE** extracted to files! 🎉
  - `backend/` - Python backend files (app.py, models.py, auth.py, etc.)
  - `frontend/` - React frontend files (pages/, components/, etc.)
  - `docker-compose.yml` - Ready to run with Docker
  - `.env.example` - Environment configuration template
  - `README.md` - Setup and run instructions

## Viewing Demo Results

After the demo completes:

```bash
# List all demo artifacts
ls artifacts/demo/

# View the actual platform code (runnable files!)
ls artifacts/demo/platform_code/
ls artifacts/demo/platform_code/backend/
ls artifacts/demo/platform_code/frontend/

# View design documentation
cat artifacts/demo/learning_objectives.md
cat artifacts/demo/backend_implementation.md

# Run the platform immediately!
cd artifacts/demo/platform_code
cp .env.example .env
# Edit .env with your settings
docker-compose up
# Platform runs on http://localhost:3000
```

## Rerunning the Demo (Ultra-Fast Artifact Skipping)

The demo is **extremely fast** when artifacts already exist! If you run it again:

```bash
python run_demo.py
```

**What happens:**
- Checks artifacts in ~4ms per phase (BEFORE creating agents)
- Skips entire phases instantly if artifacts exist
- Only runs crews for phases with missing artifacts
- Total skip time: ~1-2 seconds (vs minutes of agent creation)

For example:
- If Phase 1-3 are complete: Skips in ~1 second, then runs only Phases 4-5
- If all phases complete: Entire demo finishes in ~2 seconds with $0 cost
- If you want to regenerate specific artifacts, just delete them first

### Forcing Full Regeneration

To regenerate all artifacts from scratch:

```bash
# Delete all demo artifacts
rm -rf artifacts/demo/

# Run demo
python run_demo.py
```

### Regenerating Specific Phases

To regenerate only Phase 5 (implementation code):

```bash
# Delete Phase 5 artifacts
rm artifacts/demo/implementation_plan.md
rm artifacts/demo/backend_implementation.md
rm artifacts/demo/frontend_implementation.md
rm artifacts/demo/deployment_setup.md

# Run demo - it will skip Phases 1-4 and only run Phase 5
python run_demo.py
```

## Next Steps After Demo

### 1. Run the Platform!

The demo automatically extracts all code to runnable files:

```bash
cd artifacts/demo/platform_code

# Review the generated code structure
tree .  # or ls -R

# Setup environment
cp .env.example .env
# Edit .env to add your API keys and configuration

# Option A: Run with Docker (recommended)
docker-compose up

# Option B: Run locally
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (separate terminal)
cd frontend
npm install
npm run dev

# Platform should be running!
# Frontend: http://localhost:3000
# Backend API: http://localhost:5000
```

### 2. Review the Design Documentation

Read through the generated markdown files to understand what each crew produces:

```bash
# Quick overview of design docs
ls artifacts/demo/*.md

# Read specific documents
cat artifacts/demo/learning_objectives.md
cat artifacts/demo/system_architecture.md
cat artifacts/demo/implementation_plan.md
```

### 3. Compare with Production

Run the full production version to see the difference in depth:

```bash
python main.py run
```

Compare design documentation:
```bash
diff artifacts/demo/learning_objectives.md artifacts/learning_objectives.md
```

Note: Production mode (phase 1-4) generates design docs only, not implementation code.

### 4. Evaluate the CrewAI Workflow

The demo demonstrates:
- ✅ **Multi-agent collaboration** - 13 specialized agents working together
- ✅ **Sequential task execution** - Tasks with dependencies
- ✅ **Context passing** - Later tasks build on earlier outputs
- ✅ **State management** - Resumability and crash recovery
- ✅ **Cost tracking** - Detailed logging of LLM usage
- ✅ **Artifact generation** - Markdown documentation output

### 5. Check Logs and Costs

```bash
# View demo execution logs
ls logs/Demo*.log

# Check LLM API costs
cat logs/llm_calls.jsonl | tail -20

# Get cost summary (if you ran from main.py)
python main.py cost-report
```

## Troubleshooting

### Demo Fails to Start

**Error**: `No LLM API keys found`
**Solution**: Ensure `.env` file has either `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` set

**Error**: `ModuleNotFoundError: No module named 'crewai'`
**Solution**: Install dependencies: `pip install -r requirements.txt`

### Demo Runs But Tasks Fail

**Error**: Rate limit errors from APIs
**Solution**: The demo uses rate limiting. If errors persist:
1. Check your API tier limits
2. Increase `TASK_DELAY_SECONDS` in `.env`
3. Reduce `ANTHROPIC_RATE_LIMIT` or `OPENAI_RATE_LIMIT` in `.env`

**Error**: Tasks produce empty outputs
**Solution**: Check `logs/Demo*.log` files for detailed error messages

### Demo Stops Mid-Execution

The demo uses state management for resumability. To resume:

```bash
# The demo doesn't support resume yet, but you can check state
python main.py status
```

Currently, re-running `python run_demo.py` will skip already completed tasks.

## Understanding Demo Output Quality

### What Demo Shows

✅ **Workflow execution** - All agents, crews, and tasks run successfully
✅ **Agent specialization** - Each agent demonstrates its role
✅ **Task dependencies** - Sequential processing with context
✅ **Artifact generation** - Real markdown files created
✅ **Cost tracking** - Full instrumentation and logging

### What Demo Doesn't Show

⚠️ **Full output depth** - Outputs are 20-30% of production length
⚠️ **Complete coverage** - Examples vs comprehensive analysis
⚠️ **Extended reasoning** - Max iterations reduced (5 vs 15)

**For production evaluation**, run the full version:
```bash
python main.py run
```

## Demo Architecture

### Files Added for Demo

```
ai_mastery_platform/
├── run_demo.py                 # Demo entry point
├── demo_config.py              # Demo configuration
├── demo_profile.py             # Quick profile collection
├── tasks/
│   └── demo_tasks.py           # Simplified task definitions
├── crews/
│   └── demo_crews.py           # Demo crew runners
└── artifacts/
    └── demo/                   # Demo outputs (separate from production)
```

### Production Files (Untouched)

All production files remain unchanged:
- `main.py` - Production CLI
- `core/` - All core infrastructure
- `agents/` - All agent definitions
- `tasks/*.py` - Production task definitions (except demo_tasks.py)
- `crews/*.py` - Production crew runners (except demo_crews.py)

## Manual Code Extraction (if needed)

If for some reason the automatic extraction fails, you can extract manually:

```bash
python utils/extract_platform_code.py
```

This will read the markdown files in `artifacts/demo/` and extract all code blocks to `artifacts/demo/platform_code/`.

## FAQ

**Q: Does the demo create actual runnable code?**
A: YES! The demo generates markdown documentation AND automatically extracts all code to runnable files in `artifacts/demo/platform_code/`. You can run it immediately with Docker.

**Q: Will demo mode affect my production artifacts?**
A: No. Demo outputs go to `artifacts/demo/`, keeping production `artifacts/` clean.

**Q: Can I run both demo and production?**
A: Yes. They are completely independent. Run demo first, then production.

**Q: Do I need both OpenAI and Anthropic API keys?**
A: You need at least one. The platform uses GPT-4o for some agents and Claude Sonnet 4.5 for others. If you only have one provider's key, agents will fail for the missing provider.

**Q: How accurate is the cost estimate?**
A: The $5-10 estimate assumes:
- API pricing as of January 2025
- ~400 words average output per task
- ~5 iterations per agent
- Actual costs depend on response lengths and token usage

**Q: Can I customize the demo?**
A: Yes! Edit `demo_config.py` to adjust:
- `DEMO_MAX_ITERATIONS` - Agent reasoning depth
- `DEMO_TARGET_WORDS` - Expected output length
- `DEMO_QUICK_PROFILE` - Profile collection mode

**Q: How long does production mode take?**
A: Full production run: 30-60 minutes, depending on API speed and iteration counts.

## Support

For issues or questions:
1. Check logs: `logs/Demo*.log`
2. Review main README: `README.md`
3. Check production quickstart: `QUICKSTART.md`

---

**Ready to evaluate the full CrewAI workflow? Run the demo!**

```bash
python run_demo.py
```
