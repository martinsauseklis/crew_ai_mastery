from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, tool
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, FileReadTool, FileWriterTool, ScrapeWebsiteTool
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

MISSION_PROMPT = """I am becoming an elite AI tech leader.

I stay current with cutting-edge AI developments, frameworks, and tools from respected and vetted sources. I build strong technical foundations so I can work interchangeably with many platforms and rapidly create prototypes, tools, and automations that deliver real results.

My company is my acceleration environment.

I use the challenges, data, workflows, and opportunities inside my organization as a live laboratory for applied AI. I leverage internal projects to build real credibility, produce measurable value, and demonstrate practical mastery. Every solution I deliver becomes evidence of my ability to transform operations, culture, and business outcomes with AI.

I build systems, not random experience.

I develop strong mental models, frameworks, and systems thinking so I can quickly identify high-ROI AI opportunities across teams and functions. I focus on habits and execution discipline so excellence becomes my default operating standard, not something that requires motivation.

I lead through impact.

I communicate with both engineers and business leaders, translating technical complexity into clear business value. I mentor others, influence direction, and become a multiplier — not only solving problems, but enabling others to solve more.

I move fast with intention.

I build MVPs quickly, test assumptions, measure value, and iterate. I document learnings, share insights internally, and create reusable architectures, workflows, and playbooks.

I build reputation inside and outside my company.

The solutions I build, the results I create, and the insights I publish establish me as someone worth learning from and working with. My work becomes visible across Latvia's tech ecosystem through speaking, writing, open-source contributions, and real demonstrable impact. My reputation grows because my results speak louder than my intentions.

Recognition and mastery follow momentum.

Top 0.5% mastery is not the final goal — it is an early milestone. I evolve my skills continuously, stay adaptive, maintain long-term stamina, and protect the curiosity that drives innovation.

I am building a career that compounds.

Every tool, project, habit, and relationship strengthens my position as a respected AI solutions leader. Step by step, I become the person companies want to collaborate with — not because of promises, but because of proof."""


@CrewBase
class AiMasteryPlatform():
    """AiMasteryPlatform crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @tool
    def serper_search_tool(self):
        return SerperDevTool()

    @tool
    def scrape_website_tool(self):
        return ScrapeWebsiteTool()

    @tool
    def file_read_tool(self):
        return FileReadTool()

    @tool
    def file_write_tool(self):
        return FileWriterTool()

    @agent
    def master_orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config['master_orchestrator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def strategic_systems_team(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_systems_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def technical_execution_team(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_execution_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def impact_acceleration_team(self) -> Agent:
        return Agent(
            config=self.agents_config['impact_acceleration_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reputation_network_team(self) -> Agent:
        return Agent(
            config=self.agents_config['reputation_network_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def habits_discipline_team(self) -> Agent:
        return Agent(
            config=self.agents_config['habits_discipline_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['judge_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def revision_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['revision_coach'], # type: ignore[index]
            verbose=True
        )

    @agent
    def final_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['final_synthesizer'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def orchestration_kickoff(self) -> Task:
        return Task(
            config=self.tasks_config['orchestration_kickoff'], # type: ignore[index]
        )

    @task
    def round_1_strategic_systems_plan(self) -> Task:
        task = Task(
            config=self.tasks_config['round_1_strategic_systems_plan'], # type: ignore[index]
        )
        task.description = task.description + f"\n\nPRIMARY MISSION PROMPT:\n{MISSION_PROMPT}"
        return task

    @task
    def round_1_technical_execution_plan(self) -> Task:
        task = Task(
            config=self.tasks_config['round_1_technical_execution_plan'], # type: ignore[index]
        )
        task.description = task.description + f"\n\nPRIMARY MISSION PROMPT:\n{MISSION_PROMPT}"
        return task

    @task
    def round_1_impact_acceleration_plan(self) -> Task:
        task = Task(
            config=self.tasks_config['round_1_impact_acceleration_plan'], # type: ignore[index]
        )
        task.description = task.description + f"\n\nPRIMARY MISSION PROMPT:\n{MISSION_PROMPT}"
        return task

    @task
    def round_1_reputation_network_plan(self) -> Task:
        task = Task(
            config=self.tasks_config['round_1_reputation_network_plan'], # type: ignore[index]
        )
        task.description = task.description + f"\n\nPRIMARY MISSION PROMPT:\n{MISSION_PROMPT}"
        return task

    @task
    def round_1_habits_discipline_plan(self) -> Task:
        task = Task(
            config=self.tasks_config['round_1_habits_discipline_plan'], # type: ignore[index]
        )
        task.description = task.description + f"\n\nPRIMARY MISSION PROMPT:\n{MISSION_PROMPT}"
        return task

    @task
    def round_1_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config['round_1_evaluation'], # type: ignore[index]
        )

    @task
    def round_2_coaching_session(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_coaching_session'], # type: ignore[index]
        )

    @task
    def round_2_strategic_systems_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_strategic_systems_plan'], # type: ignore[index]
        )

    @task
    def round_2_technical_execution_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_technical_execution_plan'], # type: ignore[index]
        )

    @task
    def round_2_impact_acceleration_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_impact_acceleration_plan'], # type: ignore[index]
        )

    @task
    def round_2_reputation_network_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_reputation_network_plan'], # type: ignore[index]
        )

    @task
    def round_2_habits_discipline_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_habits_discipline_plan'], # type: ignore[index]
        )

    @task
    def round_2_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config['round_2_evaluation'], # type: ignore[index]
        )

    @task
    def round_3_coaching_session(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_coaching_session'], # type: ignore[index]
        )

    @task
    def round_3_strategic_systems_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_strategic_systems_plan'], # type: ignore[index]
        )

    @task
    def round_3_technical_execution_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_technical_execution_plan'], # type: ignore[index]
        )

    @task
    def round_3_impact_acceleration_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_impact_acceleration_plan'], # type: ignore[index]
        )

    @task
    def round_3_reputation_network_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_reputation_network_plan'], # type: ignore[index]
        )

    @task
    def round_3_habits_discipline_plan(self) -> Task:
        return Task(
            config=self.tasks_config['round_3_habits_discipline_plan'], # type: ignore[index]
        )

    @task
    def final_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config['final_evaluation'], # type: ignore[index]
        )

    @task
    def master_synthesis(self) -> Task:
        return Task(
            config=self.tasks_config['master_synthesis'], # type: ignore[index]
            output_file='MASTER_PLAN.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiMasteryPlatform crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
