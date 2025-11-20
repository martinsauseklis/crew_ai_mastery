"""Centralized LLM client with cost tracking and analytics."""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, List
from collections import defaultdict, deque

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.outputs import LLMResult

from .config import Config
from .logging_utils import get_logger

logger = get_logger(__name__)


class TokenTrackingCallback(BaseCallbackHandler):
    """
    LangChain callback handler to track token usage and costs.
    """

    def __init__(self, llm_client: 'LLMClient', agent_name: str, model: str):
        """
        Initialize callback handler.

        Args:
            llm_client: Reference to LLMClient for logging
            agent_name: Name of the agent making calls
            model: Model being used
        """
        self.llm_client = llm_client
        self.agent_name = agent_name
        self.model = model

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """
        Called when LLM completes a call.

        Args:
            response: LLM response with token usage
            **kwargs: Additional arguments
        """
        # Extract token usage from response
        if hasattr(response, 'llm_output') and response.llm_output:
            token_usage = response.llm_output.get('token_usage', {})
            if token_usage:
                prompt_tokens = token_usage.get('prompt_tokens', 0)
                completion_tokens = token_usage.get('completion_tokens', 0)

                # Get response preview
                response_text = ""
                if response.generations and len(response.generations) > 0:
                    if len(response.generations[0]) > 0:
                        response_text = str(response.generations[0][0].text)

                # Log the call
                self.llm_client.log_call(
                    agent_name=self.agent_name,
                    model=self.model,
                    input_tokens=prompt_tokens,
                    output_tokens=completion_tokens,
                    prompt_preview="",
                    response_preview=response_text[:100]
                )


class RateLimiter:
    """
    Token bucket rate limiter for API calls.
    Tracks token usage per minute and enforces rate limits.
    """

    def __init__(self, tokens_per_minute: int = 8000):
        """
        Initialize rate limiter.

        Args:
            tokens_per_minute: Maximum tokens allowed per minute
        """
        self.tokens_per_minute = tokens_per_minute
        self.token_usage = deque()  # List of (timestamp, tokens) tuples

    def _clean_old_usage(self):
        """Remove usage records older than 1 minute."""
        cutoff_time = datetime.now() - timedelta(minutes=1)
        while self.token_usage and self.token_usage[0][0] < cutoff_time:
            self.token_usage.popleft()

    def get_current_usage(self) -> int:
        """Get token usage in the last minute."""
        self._clean_old_usage()
        return sum(tokens for _, tokens in self.token_usage)

    def wait_if_needed(self, estimated_tokens: int = 2000):
        """
        Wait if adding estimated tokens would exceed rate limit.

        Args:
            estimated_tokens: Estimated tokens for the next request
        """
        self._clean_old_usage()
        current_usage = self.get_current_usage()

        if current_usage + estimated_tokens > self.tokens_per_minute:
            # Calculate how long to wait
            if self.token_usage:
                oldest_timestamp = self.token_usage[0][0]
                wait_time = 60 - (datetime.now() - oldest_timestamp).total_seconds()

                if wait_time > 0:
                    logger.info(
                        f"Rate limit approaching ({current_usage}/{self.tokens_per_minute} tokens used). "
                        f"Waiting {wait_time:.1f}s to avoid rate limit..."
                    )
                    time.sleep(wait_time + 1)  # Add 1 second buffer
                    self._clean_old_usage()

    def record_usage(self, tokens: int):
        """
        Record token usage.

        Args:
            tokens: Number of tokens used
        """
        self.token_usage.append((datetime.now(), tokens))


class LLMClient:
    """
    Wrapper around LLM API calls with built-in cost tracking and analytics.
    All agents should use this client instead of calling LLM APIs directly.
    """

    def __init__(self, logs_path: Optional[Path] = None):
        """
        Initialize the LLM client.

        Args:
            logs_path: Path to JSONL file for logging LLM calls
        """
        self.logs_path = logs_path or Config.LLM_LOGS_PATH
        self.logs_path.parent.mkdir(parents=True, exist_ok=True)

        # Rate limiters per provider
        # Anthropic free tier: 8,000 output tokens/min
        # OpenAI typically has higher limits
        self.anthropic_limiter = RateLimiter(tokens_per_minute=Config.ANTHROPIC_RATE_LIMIT)
        self.openai_limiter = RateLimiter(tokens_per_minute=Config.OPENAI_RATE_LIMIT)

        # Runtime statistics (reset each session)
        self.session_stats = {
            "total_calls": 0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "total_cost": 0.0,
            "by_agent": defaultdict(lambda: {
                "calls": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cost": 0.0
            }),
            "by_model": defaultdict(lambda: {
                "calls": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cost": 0.0
            })
        }

    def get_llm(
        self,
        model: Optional[str] = None,
        temperature: float = 0.7,
        agent_name: str = "unknown",
        **kwargs
    ):
        """
        Get a configured LangChain LLM instance with rate limiting and token tracking.

        Args:
            model: Model name (e.g., 'gpt-4o', 'claude-sonnet-4-5-20250929')
            temperature: Temperature for generation
            agent_name: Name of the agent for tracking purposes
            **kwargs: Additional parameters for the LLM

        Returns:
            Configured LangChain LLM instance with callbacks
        """
        model = model or Config.DEFAULT_MODEL

        # Estimate tokens for rate limiting (conservative estimate)
        estimated_output_tokens = kwargs.pop('estimated_tokens', 2000)

        # Create callback handler for token tracking
        callback = TokenTrackingCallback(self, agent_name, model)

        # Get existing callbacks or create new list
        callbacks = kwargs.pop('callbacks', [])
        callbacks.append(callback)

        # Route to appropriate provider
        if "gpt" in model.lower():
            if not Config.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY not set")

            # Check rate limit before creating instance
            self.openai_limiter.wait_if_needed(estimated_output_tokens)
            self.openai_limiter.record_usage(estimated_output_tokens)

            return ChatOpenAI(
                model=model,
                temperature=temperature,
                openai_api_key=Config.OPENAI_API_KEY,
                callbacks=callbacks,
                **kwargs
            )
        elif "claude" in model.lower():
            if not Config.ANTHROPIC_API_KEY:
                raise ValueError("ANTHROPIC_API_KEY not set")

            # Check rate limit before creating instance
            self.anthropic_limiter.wait_if_needed(estimated_output_tokens)
            self.anthropic_limiter.record_usage(estimated_output_tokens)

            return ChatAnthropic(
                model=model,
                temperature=temperature,
                anthropic_api_key=Config.ANTHROPIC_API_KEY,
                callbacks=callbacks,
                **kwargs
            )
        else:
            # Default to OpenAI
            if not Config.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY not set")

            self.openai_limiter.wait_if_needed(estimated_output_tokens)
            self.openai_limiter.record_usage(estimated_output_tokens)

            return ChatOpenAI(
                model=model,
                temperature=temperature,
                openai_api_key=Config.OPENAI_API_KEY,
                callbacks=callbacks,
                **kwargs
            )

    def log_call(
        self,
        agent_name: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        prompt_preview: str = "",
        response_preview: str = ""
    ):
        """
        Log an LLM API call with cost calculation.

        Args:
            agent_name: Name of the agent making the call
            model: Model used
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            prompt_preview: First 100 chars of prompt (for debugging)
            response_preview: First 100 chars of response
        """
        # Calculate cost
        costs = Config.get_model_costs(model)
        input_cost = (input_tokens / 1000.0) * costs["input"]
        output_cost = (output_tokens / 1000.0) * costs["output"]
        total_cost = input_cost + output_cost

        # Create log entry
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent_name": agent_name,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "input_cost": round(input_cost, 6),
            "output_cost": round(output_cost, 6),
            "total_cost": round(total_cost, 6),
            "prompt_preview": prompt_preview[:100],
            "response_preview": response_preview[:100]
        }

        # Append to JSONL file
        with open(self.logs_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')

        # Update session stats
        self.session_stats["total_calls"] += 1
        self.session_stats["total_input_tokens"] += input_tokens
        self.session_stats["total_output_tokens"] += output_tokens
        self.session_stats["total_cost"] += total_cost

        # By agent
        agent_stats = self.session_stats["by_agent"][agent_name]
        agent_stats["calls"] += 1
        agent_stats["input_tokens"] += input_tokens
        agent_stats["output_tokens"] += output_tokens
        agent_stats["cost"] += total_cost

        # By model
        model_stats = self.session_stats["by_model"][model]
        model_stats["calls"] += 1
        model_stats["input_tokens"] += input_tokens
        model_stats["output_tokens"] += output_tokens
        model_stats["cost"] += total_cost

        logger.debug(f"LLM call logged: {agent_name} used {model} - ${total_cost:.6f}")

    def get_session_summary(self) -> Dict[str, Any]:
        """Get summary of LLM usage for current session."""
        return {
            "total_calls": self.session_stats["total_calls"],
            "total_tokens": self.session_stats["total_input_tokens"] + self.session_stats["total_output_tokens"],
            "total_cost": round(self.session_stats["total_cost"], 4),
            "by_agent": dict(self.session_stats["by_agent"]),
            "by_model": dict(self.session_stats["by_model"])
        }

    def generate_cost_report(self, output_file: Optional[Path] = None) -> str:
        """
        Generate a detailed cost analysis report from all logged calls.

        Args:
            output_file: Optional file to write report to

        Returns:
            Report as formatted string
        """
        if not self.logs_path.exists():
            return "No LLM calls logged yet."

        # Parse all log entries
        entries = []
        with open(self.logs_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    entries.append(json.loads(line))

        if not entries:
            return "No LLM calls logged yet."

        # Aggregate statistics
        total_calls = len(entries)
        total_cost = sum(e["total_cost"] for e in entries)
        total_tokens = sum(e["total_tokens"] for e in entries)

        by_agent = defaultdict(lambda: {"calls": 0, "cost": 0.0, "tokens": 0})
        by_model = defaultdict(lambda: {"calls": 0, "cost": 0.0, "tokens": 0})
        by_day = defaultdict(lambda: {"calls": 0, "cost": 0.0, "tokens": 0})

        for entry in entries:
            agent = entry["agent_name"]
            model = entry["model"]
            day = entry["timestamp"][:10]  # YYYY-MM-DD

            by_agent[agent]["calls"] += 1
            by_agent[agent]["cost"] += entry["total_cost"]
            by_agent[agent]["tokens"] += entry["total_tokens"]

            by_model[model]["calls"] += 1
            by_model[model]["cost"] += entry["total_cost"]
            by_model[model]["tokens"] += entry["total_tokens"]

            by_day[day]["calls"] += 1
            by_day[day]["cost"] += entry["total_cost"]
            by_day[day]["tokens"] += entry["total_tokens"]

        # Build report
        report_lines = [
            "=" * 70,
            "LLM COST ANALYTICS REPORT",
            "=" * 70,
            "",
            "OVERALL SUMMARY",
            "-" * 70,
            f"Total API Calls:    {total_calls:,}",
            f"Total Tokens:       {total_tokens:,}",
            f"Total Cost:         ${total_cost:.4f}",
            "",
            "BY AGENT",
            "-" * 70,
        ]

        for agent, stats in sorted(by_agent.items(), key=lambda x: x[1]["cost"], reverse=True):
            report_lines.append(
                f"  {agent:30s} | Calls: {stats['calls']:4d} | Tokens: {stats['tokens']:8,} | Cost: ${stats['cost']:7.4f}"
            )

        report_lines.extend([
            "",
            "BY MODEL",
            "-" * 70,
        ])

        for model, stats in sorted(by_model.items(), key=lambda x: x[1]["cost"], reverse=True):
            report_lines.append(
                f"  {model:30s} | Calls: {stats['calls']:4d} | Tokens: {stats['tokens']:8,} | Cost: ${stats['cost']:7.4f}"
            )

        report_lines.extend([
            "",
            "BY DAY",
            "-" * 70,
        ])

        for day, stats in sorted(by_day.items()):
            report_lines.append(
                f"  {day} | Calls: {stats['calls']:4d} | Tokens: {stats['tokens']:8,} | Cost: ${stats['cost']:7.4f}"
            )

        report_lines.append("=" * 70)

        report = "\n".join(report_lines)

        # Write to file if requested
        if output_file:
            output_file.write_text(report, encoding='utf-8')
            logger.info(f"Cost report written to {output_file}")

        return report

    def add_task_delay(self, delay_seconds: float = 2.0):
        """
        Add a delay between tasks to help with rate limiting.

        Args:
            delay_seconds: Number of seconds to delay
        """
        logger.debug(f"Adding {delay_seconds}s delay between tasks for rate limiting")
        time.sleep(delay_seconds)
