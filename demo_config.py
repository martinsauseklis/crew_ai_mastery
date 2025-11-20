"""Demo-specific configuration for the AI Mastery Platform."""

from pathlib import Path
from core.config import Config


class DemoConfig:
    """Configuration overrides for demo mode."""

    # Demo artifacts directory (separate from production)
    DEMO_ARTIFACTS_DIR = Config.ROOT_DIR / "artifacts" / "demo"

    # Demo settings
    DEMO_MODE = True

    # Use same models as production (per user request)
    # But reduce max iterations for faster execution
    DEMO_MAX_ITERATIONS = 5  # vs 15 in production

    # Expected output lengths (rough word counts)
    DEMO_TARGET_WORDS = 400  # vs ~2000 in production

    # Skip verbose user profile - use quick 2-3 question version
    DEMO_QUICK_PROFILE = True

    @classmethod
    def ensure_demo_directories(cls):
        """Ensure demo-specific directories exist."""
        cls.DEMO_ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_demo_artifacts_dir(cls) -> Path:
        """Get the demo artifacts directory."""
        cls.ensure_demo_directories()
        return cls.DEMO_ARTIFACTS_DIR
