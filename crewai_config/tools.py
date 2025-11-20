"""
Elite Software Development Crew - Tools Definition
===================================================
This module defines all tools available to agents in the crew.
Each tool is designed for specific development tasks.
"""

from crewai_tools import (
    FileReadTool,
    FileWriterTool,
    DirectoryReadTool,
    # DirectorySearchTool,  # Disabled due to qdrant compatibility issues
    # CodeDocsSearchTool,   # Disabled due to qdrant compatibility issues
    # SerperDevTool,        # Optional web search
)
from langchain.tools import BaseTool
from typing import Any, Optional, Type
from pydantic import BaseModel, Field
import subprocess
import json
import os


# =====================================
# FILE SYSTEM TOOLS
# =====================================

filesystem_writer = FileWriterTool(
    name="Filesystem Writer",
    description="Create or update project files with content. Use for all code and documentation generation."
)

filesystem_reader = FileReadTool(
    name="Filesystem Reader",
    description="Read existing files to understand current codebase state."
)

directory_reader = DirectoryReadTool(
    name="Directory Reader",
    description="List and explore directory structures to understand project organization."
)

# Note: DirectorySearchTool and CodeDocsSearchTool disabled due to qdrant compatibility issues
# These tools require vector database features that have compatibility issues with current CrewAI version
# Agents can use filesystem_reader and local_process_executor (grep, find) as alternatives


# =====================================
# EXECUTION TOOLS
# =====================================

class ProcessExecutorInput(BaseModel):
    """Input schema for LocalProcessExecutor."""
    command: str = Field(..., description="The command to execute")
    cwd: Optional[str] = Field(None, description="Working directory (optional)")
    timeout: int = Field(300, description="Command timeout in seconds (default: 300)")


class LocalProcessExecutor(BaseTool):
    name: str = "Local Process Executor"
    description: str = "Run commands like npm install, prisma migrate, npm test, npm run build, grep, find, etc."
    args_schema: Type[BaseModel] = ProcessExecutorInput

    def _run(self, command: str, cwd: Optional[str] = None, timeout: int = 300) -> str:
        """
        Execute a command in the local environment.

        Args:
            command: The command to execute
            cwd: Working directory (optional)
            timeout: Command timeout in seconds (default: 300)

        Returns:
            JSON string with stdout, stderr, return_code, and success status
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            output = {
                "success": result.returncode == 0,
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "command": command
            }
            return json.dumps(output, indent=2)
        except subprocess.TimeoutExpired:
            output = {
                "success": False,
                "error": f"Command timed out after {timeout} seconds",
                "command": command
            }
            return json.dumps(output, indent=2)
        except Exception as e:
            output = {
                "success": False,
                "error": str(e),
                "command": command
            }
            return json.dumps(output, indent=2)


local_process_executor = LocalProcessExecutor()


# =====================================
# DATABASE TOOLS
# =====================================

class PostgresQueryInput(BaseModel):
    """Input schema for PostgresQueryTool."""
    query: str = Field(..., description="SQL query to execute")
    database_url: Optional[str] = Field(None, description="Database connection URL (optional, uses env var if not provided)")


class PostgresQueryTool(BaseTool):
    name: str = "PostgreSQL Query Tool"
    description: str = "Execute SQL queries to validate database schema or test queries."
    args_schema: Type[BaseModel] = PostgresQueryInput

    def _run(self, query: str, database_url: Optional[str] = None) -> str:
        """
        Execute a PostgreSQL query.

        Args:
            query: SQL query to execute
            database_url: Database connection URL (optional, uses env var if not provided)

        Returns:
            JSON string with query results or error
        """
        try:
            import psycopg2
            from psycopg2.extras import RealDictCursor

            db_url = database_url or os.getenv("DATABASE_URL")
            if not db_url:
                return json.dumps({
                    "success": False,
                    "error": "DATABASE_URL not provided or found in environment"
                }, indent=2)

            conn = psycopg2.connect(db_url)
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            cursor.execute(query)

            # If query returns results (SELECT), fetch them
            if cursor.description:
                results = cursor.fetchall()
                conn.close()
                return json.dumps({
                    "success": True,
                    "results": [dict(row) for row in results],
                    "row_count": len(results)
                }, indent=2)
            else:
                # For INSERT, UPDATE, DELETE, etc.
                conn.commit()
                conn.close()
                return json.dumps({
                    "success": True,
                    "message": "Query executed successfully",
                    "rows_affected": cursor.rowcount
                }, indent=2)

        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e),
                "query": query
            }, indent=2)


postgres_query = PostgresQueryTool()


# =====================================
# DOCKER TOOLS
# =====================================

class DockerCLIInput(BaseModel):
    """Input schema for DockerCLITool."""
    command: str = Field(..., description="Docker command to execute (e.g., 'compose up -d', 'ps', 'logs')")
    timeout: int = Field(300, description="Command timeout in seconds")


class DockerCLITool(BaseTool):
    name: str = "Docker CLI Tool"
    description: str = "Execute Docker commands to manage containers, images, and compose setups."
    args_schema: Type[BaseModel] = DockerCLIInput

    def _run(self, command: str, timeout: int = 300) -> str:
        """
        Execute a Docker command.

        Args:
            command: Docker command to execute (e.g., 'compose up -d', 'ps', 'logs')
            timeout: Command timeout in seconds

        Returns:
            JSON string with command output and success status
        """
        full_command = f"docker {command}"
        executor = LocalProcessExecutor()
        return executor._run(full_command, timeout=timeout)


docker_cli = DockerCLITool()


# =====================================
# GIT TOOLS
# =====================================

class GitToolInput(BaseModel):
    """Input schema for GitTool."""
    command: str = Field(..., description="Git command to execute (without 'git' prefix)")
    cwd: Optional[str] = Field(None, description="Working directory (optional)")


class GitTool(BaseTool):
    name: str = "Git Tool"
    description: str = "Execute git commands for committing, branching, and tracking changes."
    args_schema: Type[BaseModel] = GitToolInput

    def _run(self, command: str, cwd: Optional[str] = None) -> str:
        """
        Execute a git command.

        Args:
            command: Git command to execute (without 'git' prefix)
            cwd: Working directory (optional)

        Returns:
            JSON string with command output and success status
        """
        full_command = f"git {command}"
        executor = LocalProcessExecutor()
        return executor._run(full_command, cwd=cwd)


git_tool = GitTool()


# =====================================
# TESTING TOOLS
# =====================================

class JestRunnerInput(BaseModel):
    """Input schema for JestRunner."""
    test_path: Optional[str] = Field(None, description="Specific test file or directory (optional)")
    coverage: bool = Field(True, description="Generate coverage report (default: True)")
    watch: bool = Field(False, description="Run in watch mode (default: False)")


class JestRunner(BaseTool):
    name: str = "Jest Test Runner"
    description: str = "Run Jest tests with coverage reporting."
    args_schema: Type[BaseModel] = JestRunnerInput

    def _run(
        self,
        test_path: Optional[str] = None,
        coverage: bool = True,
        watch: bool = False
    ) -> str:
        """
        Run Jest tests.

        Args:
            test_path: Specific test file or directory (optional)
            coverage: Generate coverage report (default: True)
            watch: Run in watch mode (default: False)

        Returns:
            JSON string with test results and coverage information
        """
        command = "npm test"

        if test_path:
            command += f" {test_path}"

        if coverage:
            command += " -- --coverage"

        if watch:
            command += " -- --watch"

        executor = LocalProcessExecutor()
        result_str = executor._run(command)
        result = json.loads(result_str)

        # Parse test results if available
        if result["success"]:
            output = {
                "success": True,
                "output": result["stdout"],
                "tests_passed": "pass" in result["stdout"].lower()
            }
        else:
            output = {
                "success": False,
                "output": result["stdout"] + result["stderr"],
                "tests_passed": False
            }
        return json.dumps(output, indent=2)


jest_runner = JestRunner()


class PlaywrightRunnerInput(BaseModel):
    """Input schema for PlaywrightRunner."""
    test_path: Optional[str] = Field(None, description="Specific test file or directory (optional)")
    headed: bool = Field(False, description="Run with browser visible (default: False)")
    debug: bool = Field(False, description="Run in debug mode (default: False)")


class PlaywrightRunner(BaseTool):
    name: str = "Playwright Test Runner"
    description: str = "Run end-to-end tests using Playwright."
    args_schema: Type[BaseModel] = PlaywrightRunnerInput

    def _run(
        self,
        test_path: Optional[str] = None,
        headed: bool = False,
        debug: bool = False
    ) -> str:
        """
        Run Playwright tests.

        Args:
            test_path: Specific test file or directory (optional)
            headed: Run with browser visible (default: False)
            debug: Run in debug mode (default: False)

        Returns:
            JSON string with test results
        """
        command = "npx playwright test"

        if test_path:
            command += f" {test_path}"

        if headed:
            command += " --headed"

        if debug:
            command += " --debug"

        executor = LocalProcessExecutor()
        result_str = executor._run(command)
        result = json.loads(result_str)

        output = {
            "success": result["success"],
            "output": result["stdout"] + result["stderr"],
            "tests_passed": result["success"]
        }
        return json.dumps(output, indent=2)


playwright_runner = PlaywrightRunner()


# =====================================
# DOCUMENTATION TOOLS
# =====================================

class MarkdownGeneratorInput(BaseModel):
    """Input schema for MarkdownGenerator."""
    title: str = Field(..., description="Document title")
    sections: str = Field(..., description="JSON string with list of sections, each with 'heading' and 'content'")
    toc: bool = Field(True, description="Include table of contents (default: True)")


class MarkdownGenerator(BaseTool):
    name: str = "Markdown Generator"
    description: str = "Create well-formatted markdown documentation with proper structure."
    args_schema: Type[BaseModel] = MarkdownGeneratorInput

    def _run(
        self,
        title: str,
        sections: str,
        toc: bool = True
    ) -> str:
        """
        Generate markdown document.

        Args:
            title: Document title
            sections: JSON string with list of sections, each with 'heading' and 'content'
            toc: Include table of contents (default: True)

        Returns:
            Formatted markdown string
        """
        # Parse sections from JSON string
        sections_list = json.loads(sections)

        md = f"# {title}\n\n"

        # Generate TOC if requested
        if toc and len(sections_list) > 1:
            md += "## Table of Contents\n\n"
            for i, section in enumerate(sections_list, 1):
                heading = section.get("heading", f"Section {i}")
                anchor = heading.lower().replace(" ", "-").replace("/", "")
                md += f"- [{heading}](#{anchor})\n"
            md += "\n"

        # Add sections
        for section in sections_list:
            heading = section.get("heading", "")
            content = section.get("content", "")

            if heading:
                md += f"## {heading}\n\n"

            md += f"{content}\n\n"

        return md


markdown_generator = MarkdownGenerator()


# =====================================
# ANALYSIS TOOLS
# =====================================

class AnalysisToolInput(BaseModel):
    """Input schema for AnalysisTool."""
    output: str = Field(..., description="The output to validate")
    criteria: str = Field(..., description="JSON string with list of validation criteria")
    context: Optional[str] = Field(None, description="Additional context for validation (optional)")


class AnalysisTool(BaseTool):
    name: str = "Analysis Tool"
    description: str = "Analyze and validate work output for quality, completeness, and correctness."
    args_schema: Type[BaseModel] = AnalysisToolInput

    def _run(
        self,
        output: str,
        criteria: str,
        context: Optional[str] = None
    ) -> str:
        """
        Validate output against criteria.

        Args:
            output: The output to validate
            criteria: JSON string with list of validation criteria
            context: Additional context for validation (optional)

        Returns:
            JSON string with validation results
        """
        # Parse criteria from JSON string
        criteria_list = json.loads(criteria)

        results = {
            "overall_valid": True,
            "criteria_checks": [],
            "issues": [],
            "suggestions": []
        }

        # Simple validation checks
        for criterion in criteria_list:
            check_result = {
                "criterion": criterion,
                "passed": True,
                "message": ""
            }

            # Example checks (can be extended)
            if "not empty" in criterion.lower() and not output.strip():
                check_result["passed"] = False
                check_result["message"] = "Output is empty"
                results["overall_valid"] = False

            if "contains" in criterion.lower():
                # Extract what should be contained
                parts = criterion.split("contains")
                if len(parts) > 1:
                    required = parts[1].strip().strip('"').strip("'")
                    if required not in output:
                        check_result["passed"] = False
                        check_result["message"] = f"Missing required content: {required}"
                        results["overall_valid"] = False

            results["criteria_checks"].append(check_result)

        return json.dumps(results, indent=2)


analysis_tool = AnalysisTool()


# =====================================
# WEB SEARCH TOOL (for research)
# =====================================

# Note: SerperDevTool disabled due to qdrant compatibility issues
# web_search = SerperDevTool(
#     name="Web Search",
#     description="Search the web for best practices, documentation, and technical solutions."
# )


# =====================================
# TOOL REGISTRY
# =====================================

ALL_TOOLS = {
    "filesystem_writer": filesystem_writer,
    "filesystem_reader": filesystem_reader,
    "directory_reader": directory_reader,
    # "directory_search": directory_search,  # Disabled - qdrant compatibility
    # "code_docs_search": code_docs_search,  # Disabled - qdrant compatibility
    "local_process_executor": local_process_executor,
    "postgres_query": postgres_query,
    "docker_cli": docker_cli,
    "git_tool": git_tool,
    "jest_runner": jest_runner,
    "playwright_runner": playwright_runner,
    "markdown_generator": markdown_generator,
    "analysis_tool": analysis_tool,
    # "web_search": web_search,  # Disabled - qdrant compatibility
}


def get_tools(tool_names: list[str]) -> list[Any]:
    """
    Get tool instances by name.

    Args:
        tool_names: List of tool names to retrieve

    Returns:
        List of tool instances
    """
    return [ALL_TOOLS[name] for name in tool_names if name in ALL_TOOLS]
