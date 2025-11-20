# Quick Start Guide

Get the AI Mastery Platform running in 5 minutes!

## Step 1: Install Dependencies

```bash
cd ai_mastery_platform
pip install -r requirements.txt
```

Or use the setup script:

```bash
python setup.py
```

## Step 2: Configure API Key

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
OPENAI_API_KEY=sk-your-actual-key-here
```

## Step 3: Run the System

**Option A: Run all phases**

```bash
python main.py run
```

This will execute all 4 phases sequentially and generate comprehensive artifacts.

**Option B: Run one phase at a time**

```bash
# Phase 1: Vision & Requirements
python main.py run-phase 1

# Phase 2: Curriculum Construction
python main.py run-phase 2

# Phase 3: Platform Build
python main.py run-phase 3

# Phase 4: QA & Refinement
python main.py run-phase 4
```

## Step 4: View Results

**Check generated artifacts:**

```bash
python main.py artifacts
```

**View cost report:**

```bash
python main.py cost-report
```

**Check system status:**

```bash
python main.py status
```

## What to Expect

### Execution Time
- **Phase 1** (Strategy): ~5-10 minutes
- **Phase 2** (Curriculum): ~15-25 minutes (5 agents working)
- **Phase 3** (Platform): ~20-30 minutes (complex technical designs)
- **Phase 4** (QA): ~10-15 minutes

**Total**: Approximately 50-80 minutes for all phases.

### Cost Estimates

Using GPT-4:
- **Phase 1**: ~$0.50-1.00
- **Phase 2**: ~$1.50-3.00
- **Phase 3**: ~$2.00-4.00
- **Phase 4**: ~$1.00-2.00

**Total**: ~$5-10 for complete run with GPT-4

💡 **Tip**: Use `gpt-3.5-turbo` for 10x cheaper execution (set in `.env`)

### Generated Artifacts

After completion, you'll have 15+ markdown documents in `artifacts/`:

```
artifacts/
├── learning_objectives.md           # Your AI mastery goals
├── prd.md                            # Product requirements
├── roadmap.md                        # Development roadmap
├── curriculum_scaffold.md            # Complete curriculum structure
├── technical_validation.md           # AI SME review
├── learning_science_overlay.md       # Cognitive science insights
├── instructional_content_outline.md  # Detailed lesson plans
├── engagement_systems.md             # Habit & motivation design
├── ux_design.md                      # User experience design
├── system_architecture.md            # Technical architecture
├── data_infrastructure.md            # Database & data design
├── ml_systems_design.md              # ML personalization
├── llm_integration_design.md         # AI tutoring design
├── mvp_implementation_plan.md        # Detailed dev plan
├── qa_comprehensive_review.md        # Quality evaluation
├── refinement_backlog.md             # Prioritized improvements
└── validation_framework.md           # Success metrics
```

## Common Issues

### "No LLM API keys found"

Make sure you've created `.env` and added your API key:

```env
OPENAI_API_KEY=sk-...
```

### Execution is slow

This is normal! The agents are:
- Analyzing requirements
- Designing curriculum
- Creating technical architectures
- Generating comprehensive documents

Each phase involves multiple LLM calls with thoughtful reasoning.

### Want to pause and resume?

Just press Ctrl+C to stop. When you rerun:

```bash
python main.py run
```

The system will **resume from where it left off** (completed tasks are skipped).

### High costs

Switch to a cheaper model in `.env`:

```env
DEFAULT_MODEL=gpt-3.5-turbo
```

Or run phases individually to control spend.

## Next Steps

After all phases complete:

1. **Review the artifacts** - Read through the generated documents
2. **Refine as needed** - Use the refinement backlog for improvements
3. **Start building** - Use the MVP implementation plan to begin development
4. **Iterate** - The system can be rerun with modified prompts/agents

## Getting Help

```bash
# See all commands
python main.py --help

# Command-specific help
python main.py run --help
python main.py run-phase --help
```

**Need more details?** See the full [README.md](README.md)

---

Ready? Let's build your AI Mastery Platform! 🚀

```bash
python main.py run
```
