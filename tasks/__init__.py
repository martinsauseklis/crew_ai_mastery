"""Task definitions for the AI Mastery Platform crews."""

from .strategy_tasks import get_strategy_tasks
from .curriculum_tasks import get_curriculum_tasks
from .platform_tasks import get_platform_tasks
from .qa_tasks import get_qa_tasks

__all__ = [
    'get_strategy_tasks',
    'get_curriculum_tasks',
    'get_platform_tasks',
    'get_qa_tasks'
]
