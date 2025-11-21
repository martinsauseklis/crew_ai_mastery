from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, FileReadTool, FileWriterTool
from .tools.ShellCommandTool import ShellCommandTool
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

web_search_tool = SerperDevTool()
file_read_tool = FileReadTool()
file_write_tool = FileWriterTool()
shell_command = ShellCommandTool()


@CrewBase
class WebDevCrew():
    """WebDevCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def web_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['web_developer'],  # type: ignore[index]
            verbose=True,
            llm="claude-sonnet-4-5-20250929",
            allow_delegation=True,
            max_iter=5
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # type: ignore[index]
            output_file='output/web_dev_crew/facts.md',
            tools=[web_search_tool, file_write_tool]
        )

    @task
    def data_source_population(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['data_source_population'],
            tools=[file_read_tool, file_write_tool],
            output_file="output/web_dev_crew/data.json"
        )

    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'],  # type: ignore[index],
            tools=[file_read_tool, file_write_tool]
        )

    @task
    def debugging_task(self) -> Task:
        return Task(
            config=self.tasks_config['debugging_task'],  # type: ignore[index],
            tools=[file_read_tool, file_write_tool, shell_command]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the WebDevCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
