from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import GithubSearchTool
from crewai_tools import DirectoryReadTool
from crewai_tools import DirectorySearchTool
from crewai_tools import FileReadTool

@CrewBase
class HierarchicalCrewAutomationForIacAndCiCdManagementCrew():
    """HierarchicalCrewAutomationForIacAndCiCdManagement crew"""

    @agent
    def repo_puller(self) -> Agent:
        return Agent(
            config=self.agents_config['repo_puller'],
            tools=[GithubSearchTool()],
        )

    @agent
    def file_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_analyzer'],
            tools=[DirectoryReadTool(), DirectorySearchTool()],
        )

    @agent
    def terraform_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['terraform_generator'],
            tools=[FileReadTool()],
        )

    @agent
    def cicd_pipeline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['cicd_pipeline_creator'],
            tools=[FileReadTool()],
        )

    @agent
    def manager_llm(self) -> Agent:
        return Agent(
            config=self.agents_config['manager_llm'],
            tools=[],
        )


    @task
    def pull_repositories(self) -> Task:
        return Task(
            config=self.tasks_config['pull_repositories'],
            tools=[GithubSearchTool()],
        )

    @task
    def analyze_directory(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_directory'],
            tools=[DirectoryReadTool(), DirectorySearchTool()],
        )

    @task
    def generate_terraform_files(self) -> Task:
        return Task(
            config=self.tasks_config['generate_terraform_files'],
            tools=[FileReadTool()],
        )

    @task
    def setup_cicd_pipelines(self) -> Task:
        return Task(
            config=self.tasks_config['setup_cicd_pipelines'],
            tools=[FileReadTool()],
        )

    @task
    def monitor_and_optimize(self) -> Task:
        return Task(
            config=self.tasks_config['monitor_and_optimize'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the HierarchicalCrewAutomationForIacAndCiCdManagement crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
