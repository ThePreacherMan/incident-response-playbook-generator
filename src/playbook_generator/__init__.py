"""Incident Response Playbook Generator package."""

from playbook_generator.generator import (
    UnsupportedIncidentTypeError,
    generate_playbook,
    render_markdown,
    save_playbook,
)
from playbook_generator.models import (
    IncidentPlaybook,
    IncidentSeverity,
    ResponsePhase,
)
from playbook_generator.templates import get_supported_incident_types


__all__ = [
    "IncidentPlaybook",
    "IncidentSeverity",
    "ResponsePhase",
    "UnsupportedIncidentTypeError",
    "generate_playbook",
    "get_supported_incident_types",
    "render_markdown",
    "save_playbook",
]

__version__ = "1.0.0"
