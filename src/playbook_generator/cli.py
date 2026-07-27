"""Command-line interface for the incident response playbook generator."""

import argparse
import sys
from pathlib import Path

from playbook_generator.generator import (
    UnsupportedIncidentTypeError,
    generate_playbook,
    render_markdown,
    save_playbook,
)
from playbook_generator.templates import get_supported_incident_types


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="incident-response-playbook-generator",
        description=(
            "Generate structured cybersecurity incident response playbooks "
            "using predefined NIST-aligned response phases."
        ),
    )

    parser.add_argument(
        "incident_type",
        nargs="?",
        help=(
            "Incident type to generate, such as phishing, malware, "
            "ransomware, brute-force, or suspicious-login."
        ),
    )

    parser.add_argument(
        "-s",
        "--severity",
        choices=["low", "medium", "high", "critical"],
        help="Override the default incident severity.",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Save the generated playbook to a Markdown file.",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="Display all supported incident types.",
    )

    return parser


def print_supported_incident_types() -> None:
    """Print all supported incident types."""

    print("Supported incident types:")

    for incident_type in get_supported_incident_types():
        print(f"  - {incident_type}")


def run_cli() -> int:
    """Run the command-line interface."""

    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        print_supported_incident_types()
        return 0

    if not args.incident_type:
        parser.error(
            "An incident type is required unless --list is used."
        )

    try:
        playbook = generate_playbook(
            incident_type=args.incident_type,
            severity=args.severity,
        )

        if args.output:
            output_path = Path(args.output)

            if output_path.suffix.lower() != ".md":
                output_path = output_path.with_suffix(".md")

            output_path.parent.mkdir(parents=True, exist_ok=True)

            saved_path = save_playbook(
                playbook=playbook,
                output_path=str(output_path),
            )

            print(f"Playbook saved successfully: {saved_path}")
        else:
            print(render_markdown(playbook))

        return 0

    except (UnsupportedIncidentTypeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    except OSError as error:
        print(
            f"Error: Unable to save the playbook. {error}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(run_cli())
