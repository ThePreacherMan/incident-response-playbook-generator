# Changelog

All notable changes to the Incident Response Playbook Generator will be documented in this file.

This project follows semantic versioning.

## [1.0.0] - 2026-07-27

### Added

- Initial release of the Incident Response Playbook Generator
- Support for five incident types:
  - Phishing
  - Malware
  - Ransomware
  - Brute-force attacks
  - Suspicious logins
- Six NIST-aligned incident response phases:
  - Preparation
  - Detection and Analysis
  - Containment
  - Eradication
  - Recovery
  - Post-Incident Review
- Default severity levels for each incident type
- Custom severity overrides
- Incident-type input normalisation
- Markdown playbook generation
- Markdown file export
- Incident documentation checklist
- Command-line interface
- Input validation and error handling
- Sample phishing incident response playbook
- Automated tests using pytest
- GitHub Actions testing for Python 3.10, 3.11, and 3.12
- Complete README documentation
- Contribution guidelines
- Security policy
- MIT Licence

### Security

- Added validation for unsupported incident types
- Added validation for invalid severity levels
- Added safe output-directory creation
- Added defensive-use and operational disclaimers
- Added private vulnerability-reporting guidance

## Planned

Future releases may include:

- Data breach playbook
- Insider threat playbook
- Web application attack playbook
- Cloud account compromise playbook
- JSON export
- HTML export
- MITRE ATT&CK mappings
- Risk scoring
- Escalation recommendations
- Organisation-specific customisation
