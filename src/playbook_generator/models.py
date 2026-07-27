"""Data models used by the incident response playbook generator."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class IncidentSeverity(str, Enum):
    """Supported incident severity levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class ResponsePhase:
    """Represents one phase of an incident response playbook."""

    name: str
    objective: str
    actions: List[str] = field(default_factory=list)


@dataclass
class IncidentPlaybook:
    """Represents a complete incident response playbook."""

    incident_type: str
    title: str
    description: str
    severity: IncidentSeverity
    phases: List[ResponsePhase] = field(default_factory=list)

    def validate(self) -> None:
        """Validate that the playbook contains the required information."""

        if not self.incident_type.strip():
            raise ValueError("Incident type cannot be empty.")

        if not self.title.strip():
            raise ValueError("Playbook title cannot be empty.")

        if not self.description.strip():
            raise ValueError("Playbook description cannot be empty.")

        if not self.phases:
            raise ValueError("A playbook must contain at least one response phase.")

        for phase in self.phases:
            if not phase.name.strip():
                raise ValueError("Response phase name cannot be empty.")

            if not phase.objective.strip():
                raise ValueError(
                    f"The objective for phase '{phase.name}' cannot be empty."
                )

            if not phase.actions:
                raise ValueError(
                    f"Phase '{phase.name}' must contain at least one action."
                )
