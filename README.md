# Incident Response Playbook Generator

A Python-based cybersecurity tool that generates structured incident response playbooks for common security threats using the NIST-aligned incident response lifecycle.

## Overview

The Incident Response Playbook Generator helps cybersecurity analysts, SOC teams, students, and organisations create consistent response procedures for common security incidents.

The tool accepts an incident type and generates a complete Markdown playbook covering:

- Preparation
- Detection and Analysis
- Containment
- Eradication
- Recovery
- Post-Incident Review
- Incident documentation checklist

The generated output can be displayed in the terminal or saved as a reusable Markdown file.

## Supported Incident Types

The current version supports:

| Incident Type | Default Severity |
|---|---|
| Phishing | Medium |
| Malware | High |
| Ransomware | Critical |
| Brute-force attack | Medium |
| Suspicious login | High |

## Key Features

- Generates structured incident response playbooks
- Uses six NIST-aligned response phases
- Provides practical response actions for each phase
- Supports severity overrides
- Normalises common incident-type formats
- Exports playbooks to Markdown
- Includes input validation and helpful error messages
- Includes automated tests with `pytest`
- Uses only the Python standard library for the main application

## Project Structure

```text
incident-response-playbook-generator/
├── examples/
│   └── sample_playbook.md
├── src/
│   └── playbook_generator/
│       ├── __init__.py
│       ├── cli.py
│       ├── generator.py
│       ├── models.py
│       └── templates.py
├── tests/
│   ├── __init__.py
│   └── test_generator.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
