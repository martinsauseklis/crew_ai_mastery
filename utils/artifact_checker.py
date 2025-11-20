"""Utility to check if phase artifacts already exist before running crews."""

from pathlib import Path
from typing import List, Dict
from demo_config import DemoConfig


def check_artifacts_exist(artifact_files: List[str]) -> Dict[str, bool]:
    """
    Check if all specified artifact files exist and are not empty.

    Args:
        artifact_files: List of artifact filenames to check

    Returns:
        Dictionary with filename as key and exists status as value
    """
    artifacts_dir = DemoConfig.get_demo_artifacts_dir()
    results = {}

    for filename in artifact_files:
        filepath = artifacts_dir / filename
        exists = filepath.exists() and filepath.stat().st_size > 100  # At least 100 bytes
        results[filename] = exists

    return results


def all_phase_artifacts_exist(phase: str) -> bool:
    """
    Check if all artifacts for a given phase exist.

    Args:
        phase: Phase name ("strategy", "curriculum", "platform", "qa", "implementation")

    Returns:
        True if all artifacts exist, False otherwise
    """
    phase_artifacts = {
        "strategy": [
            "learning_objectives.md",
            "prd.md",
            "roadmap.md"
        ],
        "curriculum": [
            "curriculum_scaffold.md",
            "technical_validation.md",
            "learning_science_overlay.md",
            "instructional_content_outline.md",
            "engagement_systems.md"
        ],
        "platform": [
            "ux_design.md",
            "system_architecture.md",
            "data_infrastructure.md",
            "ml_systems_design.md",
            "llm_integration_design.md",
            "mvp_implementation_plan.md"
        ],
        "qa": [
            "qa_comprehensive_review.md",
            "refinement_backlog.md",
            "validation_framework.md"
        ],
        "implementation": [
            "implementation_plan.md",
            "backend_implementation.md",
            "frontend_implementation.md",
            "deployment_setup.md"
        ]
    }

    if phase not in phase_artifacts:
        return False

    artifact_status = check_artifacts_exist(phase_artifacts[phase])
    return all(artifact_status.values())


def get_missing_artifacts(phase: str) -> List[str]:
    """
    Get list of missing artifacts for a phase.

    Args:
        phase: Phase name

    Returns:
        List of missing artifact filenames
    """
    phase_artifacts = {
        "strategy": [
            "learning_objectives.md",
            "prd.md",
            "roadmap.md"
        ],
        "curriculum": [
            "curriculum_scaffold.md",
            "technical_validation.md",
            "learning_science_overlay.md",
            "instructional_content_outline.md",
            "engagement_systems.md"
        ],
        "platform": [
            "ux_design.md",
            "system_architecture.md",
            "data_infrastructure.md",
            "ml_systems_design.md",
            "llm_integration_design.md",
            "mvp_implementation_plan.md"
        ],
        "qa": [
            "qa_comprehensive_review.md",
            "refinement_backlog.md",
            "validation_framework.md"
        ],
        "implementation": [
            "implementation_plan.md",
            "backend_implementation.md",
            "frontend_implementation.md",
            "deployment_setup.md"
        ]
    }

    if phase not in phase_artifacts:
        return []

    artifact_status = check_artifacts_exist(phase_artifacts[phase])
    return [filename for filename, exists in artifact_status.items() if not exists]
