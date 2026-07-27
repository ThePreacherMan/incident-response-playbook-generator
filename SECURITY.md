# Security Policy

## Supported Versions

Security updates are currently provided for the latest version of the Incident Response Playbook Generator.

| Version | Supported |
|---|---|
| 1.0.x | Yes |
| Earlier versions | No |

Users should always use the latest available release.

## Reporting a Security Vulnerability

Please do not report security vulnerabilities through public GitHub issues.

If you discover a vulnerability, report it privately by contacting the project maintainer through LinkedIn:

[Chigoziem Ibeh on LinkedIn](https://www.linkedin.com/in/chigoziem-ibeh-seo-cybersecurity/)

Include the following information where possible:

- A clear description of the vulnerability
- The affected file, feature, or version
- Steps required to reproduce the issue
- The potential security impact
- Screenshots, logs, or proof-of-concept information
- Recommended remediation, when available

Do not include:

- Real passwords
- API keys
- Authentication tokens
- Personal information
- Confidential organisational data
- Malicious payloads that could place users at unnecessary risk

## Response Process

After receiving a security report, the maintainer will aim to:

1. Acknowledge the report.
2. Review and validate the reported issue.
3. Assess its severity and impact.
4. Develop and test an appropriate fix.
5. Release the correction when ready.
6. Credit the reporter when appropriate and requested.

Response times may depend on the complexity and severity of the vulnerability.

## Responsible Disclosure

Security researchers are asked to allow reasonable time for investigation and remediation before publicly disclosing a vulnerability.

Testing must be limited to systems, repositories, accounts, and environments that you own or are explicitly authorised to assess.

Do not:

- Access another person's data
- Disrupt services
- Destroy or modify information
- Perform denial-of-service testing
- Use social engineering
- Attempt unauthorised access
- Publish sensitive vulnerability details before remediation

## Security Scope

Relevant security concerns may include:

- Unsafe file handling
- Path traversal risks
- Command injection risks
- Dependency vulnerabilities
- Input-validation weaknesses
- Unexpected exposure of sensitive information
- Insecure generated content
- Malicious modifications to incident templates
- Vulnerabilities affecting the command-line interface

General feature requests, documentation improvements, and non-security bugs should be submitted through GitHub Issues.

## Generated Playbook Disclaimer

This project generates general defensive incident-response guidance.

Generated playbooks should not be used as a substitute for:

- Professional incident-response services
- Legal advice
- Regulatory guidance
- Digital forensic investigation
- Organisational security policies
- Business continuity planning
- Emergency communication procedures

Before operational use, organisations should review and adapt generated playbooks to their environment, legal obligations, risk profile, escalation procedures, and approved security controls.

## Dependency Security

The main application uses the Python standard library.

Development and testing dependencies should be reviewed regularly and updated when necessary.

Users can inspect installed packages with:

```bash
pip list
