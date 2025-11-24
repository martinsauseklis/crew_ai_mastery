# AI Mastery Platform - Pre-Execution Checklist

## System Overview
This is a competitive multi-agent CrewAI system with:
- **9 Agents**: 5 competing planning teams + Master Orchestrator + Judge + Revision Coach + Final Synthesizer
- **23 Tasks**: 3 rounds of competitive planning with evaluation and coaching
- **2 LLM Providers**: Claude Sonnet 4.5 (strategic thinking) + GPT-4o (coordination/execution)
- **Tools**: Serper (Google Search), Website Scraping, File Read, File Write

## Pre-Execution Checklist

### 1. Environment Variables ✓
Ensure your `.env` file contains:
```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
SERPER_API_KEY=...
```

Check with:
```bash
# Verify .env file exists and has content
cat .env | grep -E "OPENAI_API_KEY|ANTHROPIC_API_KEY|SERPER_API_KEY"
```

### 2. YAML Configuration Files ✓
- `src/ai_mastery_platform/config/agents.yaml` - 9 agents with LLMs and tools assigned
- `src/ai_mastery_platform/config/tasks.yaml` - 23 tasks with proper context dependencies

### 3. Python Dependencies ✓
Verify with:
```bash
python -c "from crewai_tools import SerperDevTool, FileReadTool, FileWriterTool; print('Tools OK')"
python -c "import crewai; print('CrewAI OK')"
```

### 4. Code Structure ✓
- `src/ai_mastery_platform/crew.py` - Main crew class with all agents and tasks
- `src/ai_mastery_platform/main.py` - Entry point for execution
- Tool imports and initialization are in place

## Agent & LLM Assignments

| Agent | LLM | Tools | Purpose |
|-------|-----|-------|---------|
| master_orchestrator | gpt-4o | file_write | Coordinate workflow |
| strategic_systems_team | claude-sonnet-4.5 | serper, scrape, file_read, file_write | Systems thinking & frameworks |
| technical_execution_team | gpt-4o | serper, scrape, file_read, file_write | Technical prototyping strategies |
| impact_acceleration_team | claude-sonnet-4.5 | serper, scrape, file_read, file_write | Business value & ROI |
| reputation_network_team | gpt-4o | serper, scrape, file_read, file_write | Reputation & community building |
| habits_discipline_team | claude-sonnet-4.5 | serper, scrape, file_read, file_write | Execution habits & discipline |
| judge_agent | claude-sonnet-4.5 | file_read, file_write | Evaluate & score plans |
| revision_coach | gpt-4o | file_read | Guide improvements |
| final_synthesizer | claude-sonnet-4.5 | file_read, file_write | Create master plan |

## Execution Workflow

The system runs 3 competitive rounds:

**Round 1** → Initial Plans (800 words each)
- 5 teams create plans
- Judge scores and provides feedback
- Coach guides teams

**Round 2** → Revised Plans (1000 words each)
- Teams improve based on feedback
- Judge re-evaluates progress
- Coach provides final guidance

**Round 3** → Final Plans (1200 words each)
- Teams deliver best work
- Judge provides final ranking
- Synthesizer creates unified master plan (3000+ words)

## Expected Outputs

Final output will be saved to:
```
MASTER_PLAN.md
```

This file will contain the synthesized master strategy integrating the best elements from all competing teams.

## Common Issues & Solutions

### Issue: "API Key not found"
**Solution**: Ensure `.env` file is in the project root and contains all three API keys

### Issue: "Module not found: crewai_tools"
**Solution**: Run `pip install crewai[tools]` or check your virtual environment

### Issue: "YAML parsing error"
**Solution**: YAML files have been validated. If you edited them, check indentation (use spaces, not tabs)

### Issue: "Claude model not found"
**Solution**: Verify ANTHROPIC_API_KEY is valid and has access to claude-sonnet-4-5-20250929

## Run the System

```bash
# From project root
crewai run
```

Expected runtime: 30-60 minutes depending on API response times and model thinking time.

## Monitoring Execution

The system runs with `verbose=True`, so you'll see:
- Agent thinking processes
- Tool calls (searches, file operations)
- Task completions
- Evaluation scores
- Final synthesis

## Cost Estimate

Approximate API costs per full run:
- Claude Sonnet 4.5: ~$10-20 (majority of tokens)
- GPT-4o: ~$3-5
- Serper searches: ~$0.50

Total: **~$15-25 per complete execution**

## Ready to Run

All checks passed! Execute with:
```bash
crewai run
```
