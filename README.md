# AI Mastery Platform - Multi-Agent Development System

A production-ready, modular CrewAI-based system that orchestrates 13+ specialized AI agents across 4 phases to design and plan a comprehensive AI learning platform. Built with fault tolerance, cost tracking, and crash recovery.

## 🎯 Overview

This system implements a complete "virtual team" that works together to design your personalized AI Mastery learning platform. The team is organized into 4 specialized crews:

- **StrategyCrew** - Vision & requirements (Chief of Staff, Product Manager)
- **CurriculumCrew** - Learning design (5 specialized learning science agents)
- **PlatformCrew** - Technical architecture (5 engineering agents)
- **QACrew** - Testing & refinement (QA Researcher)

### Key Features

✅ **Modular Architecture** - Small, focused crews instead of monolithic execution
✅ **Cost Tracking** - Detailed LLM usage analytics and spend reporting
✅ **Crash Recovery** - SQLite-backed checkpointing allows resuming from interruptions
✅ **Comprehensive Logging** - Structured logs per crew with full audit trail
✅ **Production Ready** - Complete, runnable code with proper error handling

## 🏗️ Project Structure

```
ai_mastery_platform/
├── core/                          # Core infrastructure
│   ├── config.py                  # Configuration & API keys
│   ├── state_manager.py           # Checkpointing & resumability
│   ├── llm_client.py              # LLM wrapper with cost tracking
│   └── logging_utils.py           # Structured logging
├── agents/                        # Agent definitions (13 specialized agents)
│   ├── chief_of_staff.py
│   ├── learning_agents.py         # 5 learning R&D agents
│   ├── product_agents.py          # Product Manager, UX Designer
│   ├── engineering_agents.py     # 4 engineering agents
│   └── qa_agents.py               # QA Researcher
├── tasks/                         # Task definitions by phase
│   ├── strategy_tasks.py          # Phase 1 tasks
│   ├── curriculum_tasks.py        # Phase 2 tasks
│   ├── platform_tasks.py          # Phase 3 tasks
│   └── qa_tasks.py                # Phase 4 tasks
├── crews/                         # Crew orchestration
│   ├── strategy_crew.py
│   ├── curriculum_crew.py
│   ├── platform_crew.py
│   └── qa_crew.py
├── artifacts/                     # Generated outputs (markdown docs)
├── logs/                          # Execution logs
├── data/                          # State database
├── main.py                        # CLI entry point
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- An OpenAI API key OR Anthropic API key

### Installation

1. **Clone or create the project directory:**

```bash
cd ai_mastery_platform
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure API keys:**

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API key(s):

```env
OPENAI_API_KEY=sk-your-key-here
# OR
ANTHROPIC_API_KEY=your-key-here
```

### Running the System

**Run all 4 phases sequentially:**

```bash
python main.py run
```

This will execute:
- Phase 1: Vision & Requirements (StrategyCrew)
- Phase 2: Curriculum Construction (CurriculumCrew)
- Phase 3: Product & Platform Build (PlatformCrew)
- Phase 4: Testing & Refinement (QACrew)

**Run a specific phase:**

```bash
python main.py run-phase 1  # Just Phase 1
python main.py run-phase 2  # Just Phase 2
# etc.
```

**Check system status:**

```bash
python main.py status
```

**View generated artifacts:**

```bash
python main.py artifacts
```

**Generate cost report:**

```bash
python main.py cost-report
python main.py cost-report -o cost_report.txt  # Save to file
```

## 📊 What Gets Generated

The system generates comprehensive markdown documents in the `artifacts/` directory:

### Phase 1: Vision & Requirements
- `learning_objectives.md` - Comprehensive learning objectives mapped to Bloom's taxonomy
- `prd.md` - Product Requirements Document with features, user stories, success metrics
- `roadmap.md` - Multi-phase product roadmap

### Phase 2: Curriculum Construction
- `curriculum_scaffold.md` - Complete curriculum structure with modules and topics
- `technical_validation.md` - AI SME review of technical depth and industry relevance
- `learning_science_overlay.md` - Cognitive science principles applied to curriculum
- `instructional_content_outline.md` - Detailed lesson plans and learning activities
- `engagement_systems.md` - Behavior design for habit formation and motivation

### Phase 3: Product & Platform Build
- `ux_design.md` - User experience design, wireframes, and design system
- `system_architecture.md` - Technical architecture and technology stack
- `data_infrastructure.md` - Database schema and data pipelines
- `ml_systems_design.md` - Machine learning personalization systems
- `llm_integration_design.md` - LLM-powered tutoring and content generation
- `mvp_implementation_plan.md` - Detailed MVP development plan

### Phase 4: Testing & Refinement
- `qa_comprehensive_review.md` - Multi-dimensional evaluation of all work
- `refinement_backlog.md` - Prioritized improvements and recommendations
- `validation_framework.md` - Metrics and evaluation protocols

## 🔄 Crash Recovery & Resumability

The system uses SQLite to checkpoint progress. If execution is interrupted:

1. **State is preserved** - All completed tasks are marked in the database
2. **Resume automatically** - Rerun the same command; completed tasks are skipped
3. **View progress** - Use `python main.py status` to see what's done

Example:

```bash
# Start execution
python main.py run

# ... system crashes or is interrupted ...

# Resume - picks up where it left off
python main.py run
```

The state database is stored at `data/state.db`.

## 💰 Cost Tracking

Every LLM API call is logged with:
- Timestamp
- Agent name
- Model used
- Input/output tokens
- Estimated cost

**View session summary:**

Automatically displayed after each run.

**Generate detailed report:**

```bash
python main.py cost-report
```

Sample output:

```
======================================================================
LLM COST ANALYTICS REPORT
======================================================================

OVERALL SUMMARY
----------------------------------------------------------------------
Total API Calls:    47
Total Tokens:       125,340
Total Cost:         $3.2450

BY AGENT
----------------------------------------------------------------------
  Curriculum Architect           | Calls:   12 | Tokens:   34,120 | Cost: $1.0236
  Product Manager                | Calls:    8 | Tokens:   22,450 | Cost: $0.6735
  ...
```

Logs are stored in `logs/llm_calls.jsonl` for further analysis.

## 🧪 Development & Customization

### Modify Agent Behavior

Edit agent definitions in `agents/`:

```python
# agents/curriculum_agents.py

def create_curriculum_architect(llm_client: LLMClient) -> Agent:
    return Agent(
        role="Curriculum Architect",
        goal="...",  # Modify the goal
        backstory="...",  # Customize backstory
        llm=llm_client.get_llm(model="gpt-4", temperature=0.6)  # Change model
    )
```

### Add New Tasks

Edit task definitions in `tasks/`:

```python
# tasks/strategy_tasks.py

def get_strategy_tasks(chief_of_staff, product_manager) -> list:
    new_task = Task(
        description="Your custom task description",
        expected_output="What the task should produce",
        agent=product_manager,
        output_file=str(Config.ARTIFACTS_DIR / "custom_output.md")
    )
    return [existing_tasks..., new_task]
```

### Change LLM Models

Update `.env`:

```env
DEFAULT_MODEL=gpt-3.5-turbo  # Cheaper option
# or
DEFAULT_MODEL=claude-3-opus  # Anthropic Claude
```

Or specify per-agent in agent definitions.

### Adjust Cost Prices

Update `core/config.py`:

```python
LLM_COSTS: Dict[str, Dict[str, float]] = {
    "gpt-4": {"input": 0.03, "output": 0.06},
    # Add new models or update prices
}
```

## 📝 Logging

Logs are written to `logs/`:

- `main.log` - Overall orchestration
- `StrategyCrew.log` - Phase 1 logs
- `CurriculumCrew.log` - Phase 2 logs
- `PlatformCrew.log` - Phase 3 logs
- `QACrew.log` - Phase 4 logs
- `llm_calls.jsonl` - All LLM API calls

Set log level in `.env`:

```env
LOG_LEVEL=DEBUG  # For verbose debugging
```

## 🛠️ Troubleshooting

### "No LLM API keys found"

Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` in your `.env` file.

### Crew execution hangs

Check `logs/<crew_name>.log` for details. The agents may be waiting on LLM responses. Ensure your API key has sufficient quota.

### Want to reset and start over

Delete the state database:

```bash
rm data/state.db
```

Then rerun:

```bash
python main.py run
```

### Cost is too high

- Use `gpt-3.5-turbo` instead of `gpt-4` (10x cheaper)
- Set `DEFAULT_MODEL=gpt-3.5-turbo` in `.env`
- Run phases individually to control spend
- Simplify task descriptions to reduce token usage

## 🏢 Architecture Details

### Modular Crews

Instead of one massive crew with all 13 agents, the system uses **4 specialized crews**:

1. **StrategyCrew** (2 agents) - Lightweight, defines high-level vision
2. **CurriculumCrew** (5 agents) - Focused on learning design
3. **PlatformCrew** (5 agents) - Technical architecture and engineering
4. **QACrew** (1 agent) - Evaluation and refinement

Each crew:
- Runs independently
- Has its own log file
- Updates shared state via StateManager
- Can be run individually for debugging

### State Management

SQLite database (`data/state.db`) tracks:

- **Tasks**: crew_name, task_id, status (pending/in_progress/completed/failed)
- **Crew Runs**: run_id, status, timestamps, errors
- **Phases**: phase_number, status, timestamps

This enables:
- Resuming from crashes
- Skipping completed work
- Audit trail of all executions

### LLM Client Wrapper

All agents use `LLMClient` instead of calling APIs directly:

- Standardizes LLM access
- Logs every call to `llm_calls.jsonl`
- Calculates costs in real-time
- Supports multiple providers (OpenAI, Anthropic)

### Orchestration Flow

```
main.py
  ↓
initialize_system() → StateManager + LLMClient
  ↓
run_strategy_crew()
  ├─ Create agents (Chief of Staff, Product Manager)
  ├─ Create tasks (objectives, PRD, roadmap)
  ├─ Check state (skip completed tasks)
  ├─ Execute crew
  └─ Update state (mark completed)
  ↓
run_curriculum_crew()
  ├─ Create agents (5 learning specialists)
  ├─ Create tasks (curriculum, validation, etc.)
  ├─ Check state
  ├─ Execute crew
  └─ Update state
  ↓
run_platform_crew()
  ... (similar pattern)
  ↓
run_qa_crew()
  ... (similar pattern)
  ↓
print_cost_summary()
```

## 🎓 The Org Chart (13 Agents)

### Executive
- **Chief of Staff** - Strategic oversight and coordination

### Learning R&D Division
- **Curriculum Architect** - Curriculum structure and learning pathways
- **AI Subject Matter Expert** - Technical accuracy and depth
- **Instructional Designer** - Learning activities and materials
- **Cognitive Scientist** - Learning science and memory optimization
- **Behavior Designer** - Habit formation and engagement systems

### Product & Delivery Division
- **Product Manager** - Requirements and prioritization
- **UX Designer** - User experience and interface design

### Engineering & Platform Division
- **Full-Stack Developer** - Web app architecture
- **Backend/Data Engineer** - Database and data pipelines
- **ML Engineer** - Personalization and recommendation systems
- **LLM Engineer** - AI tutoring and content generation

### QA & Research
- **QA Researcher** - Evaluation and quality assurance

## 📚 Further Reading

- [CrewAI Documentation](https://docs.crewai.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude API Docs](https://docs.anthropic.com/)

## 🤝 Contributing

This is a personal learning platform system, but you can customize it for your needs:

1. Fork or copy the project
2. Modify agents, tasks, and crews to fit your domain
3. Adjust the workflows to match your process
4. Share improvements or extensions!

## 📄 License

MIT License - feel free to use and modify for your purposes.

## 🙏 Acknowledgments

Built with:
- [CrewAI](https://www.crewai.com/) - Multi-agent orchestration framework
- [LangChain](https://www.langchain.com/) - LLM integration
- [Rich](https://rich.readthedocs.io/) - Beautiful CLI output
- [Click](https://click.palletsprojects.com/) - CLI framework

---

**Ready to build your AI Mastery Platform?**

```bash
python main.py run
```

Watch as 13 specialized AI agents collaborate to design your personalized learning journey! 🚀
