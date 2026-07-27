"""Core logic for generating incident response playbooks."""

from copy import deepcopy
from typing import Optional

from playbook_generator.models import (
    IncidentPlaybook,
    IncidentSeverity,
    ResponsePhase,
)
from playbook_generator.templates import (
    PHASE_OBJECTIVES,
    PLAYBOOK_TEMPLATES,
    get_supported_incident_types,
)


class UnsupportedIncidentTypeError(ValueError):
    """Raised when the requested incident type is not supported."""


def normalise_incident_type(incident_type: str) -> str:
    """Convert an incident type into the format used by the templates."""

    normalised = incident_type.strip().lower().replace("_", "-").replace(" ", "-")

    aliases = {
        "bruteforce": "brute-force",
        "suspiciouslogin": "suspicious-login",
        "suspicious-sign-in": "suspicious-login",
        "suspicious-signin": "suspicious-login",
    }

    return aliases.get(normalised, normalised)


def parse_severity(severity: str) -> IncidentSeverity:
    """Convert a severity string into an IncidentSeverity value."""

    normalised = severity.strip().lower()

    try:
        return IncidentSeverity(normalised)
    except ValueError as error:
        supported = ", ".join(item.value for item in IncidentSeverity)

        raise ValueError(
            f"Unsupported severity '{severity}'. "
            f"Supported severity levels: {supported}."
        ) from error


def generate_playbook(
    incident_type: str,
    severity: Optional[str] = None,
) -> IncidentPlaybook:
    """Generate a structured incident response playbook.

    Args:
        incident_type: The type of cybersecurity incident.
        severity: Optional severity override.

    Returns:
        A validated IncidentPlaybook instance.

    Raises:
        UnsupportedIncidentTypeError: If the incident type is unsupported.
        ValueError: If the severity value is invalid.
    """

    normalised_type = normalise_incident_type(incident_type)

    if normalised_type not in PLAYBOOK_TEMPLATES:
        supported = ", ".join(get_supported_incident_types())

        raise UnsupportedIncidentTypeError(
            f"Unsupported incident type '{incident_type}'. "
            f"Supported incident types: {supported}."
        )

    template = deepcopy(PLAYBOOK_TEMPLATES[normalised_type])

    if severity:
        selected_severity = parse_severity(severity)
    else:
        selected_severity = template["default_severity"]

    phases = []

    for phase_name, actions in template["phases"].items():
        objective = PHASE_OBJECTIVES.get(
            phase_name,
            "Complete the required response actions for this phase.",
        )

        phases.append(
            ResponsePhase(
                name=phase_name,
                objective=objective,
                actions=list(actions),
            )
        )

    playbook = IncidentPlaybook(
        incident_type=normalised_type,
        title=str(template["title"]),
        description=str(template["description"]),
        severity=selected_severity,
        phases=phases,
    )

    playbook.validate()

    return playbook


def render_markdown(playbook: IncidentPlaybook) -> str:
    """Convert a generated playbook into Markdown format."""

    playbook.validate()

    lines = [
        f"# {playbook.title}",
        "",
        f"**Incident Type:** {playbook.incident_type}",
        "",
        f"**Severity:** {playbook.severity.value.upper()}",
        "",
        "## Description",
        "",
        playbook.description,
        "",
        "## Incident Response Phases",
        "",
    ]

    for phase_number, phase in enumerate(playbook.phases, start=1):
        lines.extend(
            [
                f"### {phase_number}. {phase.name}",
                "",
                f"**Objective:** {phase.objective}",
                "",
            ]
        )

        for action_number, action in enumerate(phase.actions, start=1):
            lines.append(f"{action_number}. {action}")

        lines.append("")

    lines.extend(
        [
            "## Incident Documentation Checklist",
            "",
            "- [ ] Record the date and time the incident was detected.",
            "- [ ] Identify the person or system that reported the incident.",
            "- [ ] Record affected users, devices, systems, and services.",
            "- [ ] Preserve relevant logs and forensic evidence.",
            "- [ ] Document containment and eradication actions.",
            "- [ ] Record all internal and external communications.",
            "- [ ] Document recovery validation results.",
            "- [ ] Record lessons learned and remediation owners.",
            "",
            "## Important Notice",
            "",
            (
                "This playbook provides general incident response guidance. "
                "Organisations should adapt the procedures to their environment, "
                "legal obligations, security policies, and escalation processes."
            ),
            "",
        ]
    )

    return "\n".join(lines)


def save_playbook(playbook: IncidentPlaybook, output_path: str) -> str:
    """Save a generated playbook as a Markdown file."""

    if not output_path.strip():
        raise ValueError("Output path cannot be empty.")

    markdown_content = render_markdown(playbook)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(markdown_content)

    return output_path
