"""Configuration management for the AI Mastery Platform."""

import os
from pathlib import Path
from typing import Dict, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Central configuration for the AI Mastery Platform."""

    # Project paths
    ROOT_DIR = Path(__file__).parent.parent
    ARTIFACTS_DIR = ROOT_DIR / "artifacts"
    LOGS_DIR = ROOT_DIR / "logs"
    DATA_DIR = ROOT_DIR / "data"
    STATE_DB_PATH = DATA_DIR / "state.db"
    LLM_LOGS_PATH = LOGS_DIR / "llm_calls.jsonl"

    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

    # LLM Configuration
    DEFAULT_LLM_PROVIDER = os.getenv("DEFAULT_LLM_PROVIDER", "anthropic")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-sonnet-4-5-20250929")

    # LLM Cost tracking (USD per 1K tokens)
    # Updated pricing as of January 2025
    LLM_COSTS: Dict[str, Dict[str, float]] = {
        # Claude models (latest)
        "claude-sonnet-4-5-20250929": {"input": 0.003, "output": 0.015},
        "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
        "claude-3-opus-20240229": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet-20240229": {"input": 0.003, "output": 0.015},
        "claude-3-haiku-20240307": {"input": 0.00025, "output": 0.00125},
        # OpenAI models
        "gpt-4o": {"input": 0.0025, "output": 0.01},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
    }

    # Crew configuration
    CREW_VERBOSE = os.getenv("CREW_VERBOSE", "true").lower() == "true"
    MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "15"))

    # Rate limiting (tokens per minute)
    ANTHROPIC_RATE_LIMIT = int(os.getenv("ANTHROPIC_RATE_LIMIT", "7500"))  # Conservative for 8k limit
    OPENAI_RATE_LIMIT = int(os.getenv("OPENAI_RATE_LIMIT", "90000"))  # Conservative for tier 1
    TASK_DELAY_SECONDS = float(os.getenv("TASK_DELAY_SECONDS", "2.0"))  # Delay between tasks

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # User profile (set at runtime)
    USER_PROFILE: Optional[Dict[str, str]] = None

    @classmethod
    def set_user_profile(cls, profile: Dict[str, str]):
        """
        Set the user profile for personalization.

        Args:
            profile: User profile dictionary
        """
        cls.USER_PROFILE = profile

    @classmethod
    def get_user_profile(cls) -> Optional[Dict[str, str]]:
        """
        Get the user profile.

        Returns:
            User profile dictionary or None
        """
        return cls.USER_PROFILE

    @classmethod
    def ensure_directories(cls):
        """Ensure all necessary directories exist."""
        cls.ARTIFACTS_DIR.mkdir(exist_ok=True)
        cls.LOGS_DIR.mkdir(exist_ok=True)
        cls.DATA_DIR.mkdir(exist_ok=True)

    @classmethod
    def validate_api_keys(cls):
        """Validate that required API keys are present."""
        if not cls.OPENAI_API_KEY and not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "No LLM API keys found. Please set OPENAI_API_KEY or ANTHROPIC_API_KEY "
                "in your environment variables or .env file."
            )
        return True

    @classmethod
    def get_model_costs(cls, model: str) -> Dict[str, float]:
        """Get cost structure for a given model."""
        # Try exact match first
        if model in cls.LLM_COSTS:
            return cls.LLM_COSTS[model]

        # Try prefix matching for versioned models
        for known_model, costs in cls.LLM_COSTS.items():
            if model.startswith(known_model):
                return costs

        # Default fallback
        return {"input": 0.01, "output": 0.03}
