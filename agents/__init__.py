"""Agent definitions for the AI Mastery Platform."""

from .chief_of_staff import create_chief_of_staff
from .learning_agents import (
    create_curriculum_architect,
    create_ai_sme,
    create_instructional_designer,
    create_cognitive_scientist,
    create_behavior_designer
)
from .product_agents import create_product_manager, create_ux_designer
from .engineering_agents import (
    create_fullstack_developer,
    create_backend_engineer,
    create_ml_engineer,
    create_llm_engineer
)
from .qa_agents import create_qa_researcher
from .implementation_agents import (
    create_implementation_architect,
    create_backend_implementer,
    create_frontend_implementer,
    create_devops_implementer
)
from .validator_agents import (
    create_backend_validator,
    create_frontend_validator,
    create_integration_validator,
    create_data_validator,
    create_debug_assistant
)

__all__ = [
    'create_chief_of_staff',
    'create_curriculum_architect',
    'create_ai_sme',
    'create_instructional_designer',
    'create_cognitive_scientist',
    'create_behavior_designer',
    'create_product_manager',
    'create_ux_designer',
    'create_fullstack_developer',
    'create_backend_engineer',
    'create_ml_engineer',
    'create_llm_engineer',
    'create_qa_researcher',
    'create_implementation_architect',
    'create_backend_implementer',
    'create_frontend_implementer',
    'create_devops_implementer',
    'create_backend_validator',
    'create_frontend_validator',
    'create_integration_validator',
    'create_data_validator',
    'create_debug_assistant'
]
