"""Tests for the incident response playbook generator."""

import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRECTORY = PROJECT_ROOT / "src"

if str(SOURCE_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIRECTORY))


from playbook_generator.generator import (
    UnsupportedIncidentTypeError,
    generate_playbook,
    normalise_incident_type,
    parse_severity,
    render_markdown,
)
from playbook_generator.models import IncidentSeverity
from playbook_generator.templates import get_supported_incident_types


def test_supported_incident_types_are_available() -> None:
    """Confirm that the expected incident types are supported."""

    supported_types = get_supported_incident_types()

    assert "phishing" in supported_types
    assert "malware" in supported_types
    assert "ransomware" in supported_types
    assert "brute-force" in supported_types
    assert "suspicious-login" in supported_types


def test_generate_phishing_playbook() -> None:
    """Confirm that a phishing playbook is generated correctly."""

    playbook = generate_playbook("phishing")

    assert playbook.incident_type == "phishing"
    assert playbook.title == "Phishing Incident Response Playbook"
    assert playbook.severity == IncidentSeverity.MEDIUM
    assert len(playbook.phases) == 6


def test_generate_ransomware_playbook() -> None:
    """Confirm that ransomware uses critical severity by default."""

    playbook = generate_playbook("ransomware")

    assert playbook.incident_type == "ransomware"
    assert playbook.severity == IncidentSeverity.CRITICAL
    assert len(playbook.phases) == 6


def test_severity_override() -> None:
    """Confirm that users can override the default severity."""

    playbook = generate_playbook(
        incident_type="phishing",
        severity="high",
    )

    assert playbook.severity == IncidentSeverity.HIGH


@pytest.mark.parametrize(
    ("provided_value", "expected_value"),
    [
        ("Brute Force", "brute-force"),
        ("brute_force", "brute-force"),
        ("bruteforce", "brute-force"),
        ("Suspicious Login", "suspicious-login"),
        ("suspicious_sign_in", "suspicious-login"),
    ],
)
def test_normalise_incident_type(
    provided_value: str,
    expected_value: str,
) -> None:
    """Confirm that common incident-type formats are normalised."""

    assert normalise_incident_type(provided_value) == expected_value


@pytest.mark.parametrize(
    ("provided_value", "expected_value"),
    [
        ("low", IncidentSeverity.LOW),
        ("MEDIUM", IncidentSeverity.MEDIUM),
        (" High ", IncidentSeverity.HIGH),
        ("critical", IncidentSeverity.CRITICAL),
    ],
)
def test_parse_valid_severity(
    provided_value: str,
    expected_value: IncidentSeverity,
) -> None:
    """Confirm that valid severity values are parsed."""

    assert parse_severity(provided_value) == expected_value


def test_invalid_severity_raises_error() -> None:
    """Confirm that unsupported severity values are rejected."""

    with pytest.raises(ValueError, match="Unsupported severity"):
        parse_severity("extreme")


def test_unsupported_incident_type_raises_error() -> None:
    """Confirm that unsupported incident types are rejected."""

    with pytest.raises(
        UnsupportedIncidentTypeError,
        match="Unsupported incident type",
    ):
        generate_playbook("unknown-incident")


def test_render_markdown_contains_required_sections() -> None:
    """Confirm that generated Markdown contains core sections."""

    playbook = generate_playbook("malware")
    markdown = render_markdown(playbook)

    assert "# Malware Incident Response Playbook" in markdown
    assert "**Severity:** HIGH" in markdown
    assert "### 1. Preparation" in markdown
    assert "### 6. Post-Incident Review" in markdown
    assert "## Incident Documentation Checklist" in markdown
    assert "## Important Notice" in markdown


def test_every_phase_has_an_objective_and_actions() -> None:
    """Confirm that every generated phase is complete."""

    playbook = generate_playbook("suspicious-login")

    for phase in playbook.phases:
        assert phase.name
        assert phase.objective
        assert phase.actions
