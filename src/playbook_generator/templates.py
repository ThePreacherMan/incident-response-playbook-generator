"""Predefined incident response playbook templates."""

from typing import Dict, List

from playbook_generator.models import IncidentSeverity


PLAYBOOK_TEMPLATES: Dict[str, Dict[str, object]] = {
    "phishing": {
        "title": "Phishing Incident Response Playbook",
        "description": (
            "Guidance for investigating, containing, and recovering from "
            "suspected phishing attacks."
        ),
        "default_severity": IncidentSeverity.MEDIUM,
        "phases": {
            "Preparation": [
                "Maintain email security controls and anti-phishing filters.",
                "Provide phishing awareness training to employees.",
                "Document escalation contacts and communication procedures.",
                "Ensure endpoint detection and response tools are operational.",
            ],
            "Detection and Analysis": [
                "Collect the suspicious email, headers, links, and attachments.",
                "Identify all recipients of the suspicious message.",
                "Check whether any user clicked a link or opened an attachment.",
                "Review authentication logs for suspicious sign-in activity.",
                "Analyse URLs, domains, attachments, and sender infrastructure.",
                "Determine whether credentials or sensitive data were exposed.",
            ],
            "Containment": [
                "Remove the phishing email from affected mailboxes.",
                "Block malicious domains, URLs, senders, and file hashes.",
                "Disable or restrict accounts showing signs of compromise.",
                "Revoke active sessions and reset exposed credentials.",
                "Isolate affected endpoints when malware execution is suspected.",
            ],
            "Eradication": [
                "Remove malicious files, browser extensions, and persistence.",
                "Scan affected systems using approved security tools.",
                "Delete unauthorised mailbox forwarding rules.",
                "Remove malicious OAuth applications and access tokens.",
                "Patch exploited software vulnerabilities where applicable.",
            ],
            "Recovery": [
                "Restore account access after credentials are secured.",
                "Monitor affected accounts and devices for recurring activity.",
                "Confirm that blocked indicators remain enforced.",
                "Notify affected users and provide secure access instructions.",
            ],
            "Post-Incident Review": [
                "Document the incident timeline, impact, and response actions.",
                "Identify security-control and awareness-training gaps.",
                "Update email filtering rules and detection procedures.",
                "Record lessons learned and assign remediation owners.",
            ],
        },
    },
    "malware": {
        "title": "Malware Incident Response Playbook",
        "description": (
            "Guidance for responding to malware detected on endpoints, "
            "servers, or other organisational systems."
        ),
        "default_severity": IncidentSeverity.HIGH,
        "phases": {
            "Preparation": [
                "Maintain current endpoint protection and EDR coverage.",
                "Keep tested system backups in protected storage.",
                "Document endpoint isolation and forensic collection procedures.",
                "Maintain an approved list of incident response tools.",
            ],
            "Detection and Analysis": [
                "Collect detection alerts, process data, and file hashes.",
                "Identify the affected host, user, and network connections.",
                "Determine the malware type and suspected initial access vector.",
                "Check for persistence, privilege escalation, and lateral movement.",
                "Search the environment for matching indicators of compromise.",
            ],
            "Containment": [
                "Isolate affected devices from the network.",
                "Block malicious IP addresses, domains, and file hashes.",
                "Disable compromised accounts where necessary.",
                "Preserve volatile data and forensic evidence.",
                "Restrict shared resources exposed to the affected system.",
            ],
            "Eradication": [
                "Terminate malicious processes and remove persistence.",
                "Delete or quarantine confirmed malicious files.",
                "Patch exploited vulnerabilities and insecure configurations.",
                "Reimage systems when complete removal cannot be verified.",
                "Reset credentials exposed on affected devices.",
            ],
            "Recovery": [
                "Restore systems from verified clean backups.",
                "Reconnect systems gradually after security validation.",
                "Monitor restored systems for suspicious activity.",
                "Confirm endpoint protection and logging are operational.",
            ],
            "Post-Incident Review": [
                "Document the malware behaviour and attack path.",
                "Update detections with discovered indicators.",
                "Review patching, access control, and endpoint-security gaps.",
                "Record lessons learned and remediation actions.",
            ],
        },
    },
    "ransomware": {
        "title": "Ransomware Incident Response Playbook",
        "description": (
            "Guidance for containing ransomware, protecting evidence, "
            "restoring operations, and limiting business impact."
        ),
        "default_severity": IncidentSeverity.CRITICAL,
        "phases": {
            "Preparation": [
                "Maintain offline or immutable backups of critical systems.",
                "Test business continuity and disaster recovery procedures.",
                "Deploy endpoint protection and centralised security logging.",
                "Document legal, executive, insurance, and law-enforcement contacts.",
            ],
            "Detection and Analysis": [
                "Identify encrypted systems, ransom notes, and affected services.",
                "Determine the likely ransomware family and entry point.",
                "Assess whether data theft occurred before encryption.",
                "Identify compromised accounts and lateral movement activity.",
                "Estimate operational, financial, and regulatory impact.",
            ],
            "Containment": [
                "Immediately isolate affected systems and network segments.",
                "Disable compromised accounts and revoke active sessions.",
                "Block known malicious infrastructure and indicators.",
                "Protect unaffected backups from modification or deletion.",
                "Preserve ransom notes, logs, memory, and disk evidence.",
            ],
            "Eradication": [
                "Remove ransomware payloads and persistence mechanisms.",
                "Patch exploited vulnerabilities and exposed services.",
                "Reset privileged and affected user credentials.",
                "Rebuild compromised systems from trusted installation media.",
                "Verify that attacker access has been fully removed.",
            ],
            "Recovery": [
                "Restore critical services from validated clean backups.",
                "Prioritise restoration using business impact requirements.",
                "Monitor rebuilt systems for renewed attacker activity.",
                "Validate system integrity before returning to production.",
                "Communicate recovery status to approved stakeholders.",
            ],
            "Post-Incident Review": [
                "Document the complete attack timeline and business impact.",
                "Review backup resilience and restoration performance.",
                "Address detection, segmentation, and access-control failures.",
                "Complete required legal and regulatory notifications.",
                "Update continuity plans and incident response procedures.",
            ],
        },
    },
    "brute-force": {
        "title": "Brute-Force Attack Response Playbook",
        "description": (
            "Guidance for investigating and responding to repeated "
            "authentication attempts against user or administrative accounts."
        ),
        "default_severity": IncidentSeverity.MEDIUM,
        "phases": {
            "Preparation": [
                "Enforce multi-factor authentication for critical accounts.",
                "Configure account lockout and rate-limiting controls.",
                "Centralise authentication and access logs.",
                "Maintain alerts for repeated failed sign-in attempts.",
            ],
            "Detection and Analysis": [
                "Identify targeted accounts, systems, and source addresses.",
                "Review failed and successful authentication events.",
                "Determine whether any login attempt succeeded.",
                "Check for password spraying across multiple accounts.",
                "Review post-authentication activity for compromised accounts.",
            ],
            "Containment": [
                "Block or rate-limit malicious source addresses.",
                "Temporarily lock targeted or compromised accounts.",
                "Revoke suspicious sessions and authentication tokens.",
                "Restrict external access to targeted services where necessary.",
            ],
            "Eradication": [
                "Reset passwords for confirmed or suspected compromised accounts.",
                "Remove unauthorised access keys and application passwords.",
                "Correct exposed services and insecure authentication settings.",
                "Apply missing security updates.",
            ],
            "Recovery": [
                "Restore account access using verified user identities.",
                "Enable or strengthen multi-factor authentication.",
                "Monitor targeted accounts for repeated attempts.",
                "Confirm legitimate users can access required services.",
            ],
            "Post-Incident Review": [
                "Document targeted accounts and successful access attempts.",
                "Review password policy and authentication controls.",
                "Update detection thresholds and blocklists.",
                "Record lessons learned and assigned improvements.",
            ],
        },
    },
    "suspicious-login": {
        "title": "Suspicious Login Incident Response Playbook",
        "description": (
            "Guidance for investigating unusual login locations, devices, "
            "times, or authentication behaviours."
        ),
        "default_severity": IncidentSeverity.HIGH,
        "phases": {
            "Preparation": [
                "Enable multi-factor authentication and conditional access.",
                "Collect identity, device, VPN, and application logs.",
                "Maintain identity-verification and account-recovery procedures.",
                "Configure alerts for unusual sign-in behaviour.",
            ],
            "Detection and Analysis": [
                "Review the login time, location, device, and source address.",
                "Compare the event with the user's normal activity.",
                "Contact the user through an approved verification channel.",
                "Check for mailbox, file, or application access after login.",
                "Determine whether authentication tokens were stolen.",
            ],
            "Containment": [
                "Revoke active sessions and refresh tokens.",
                "Temporarily disable the account when compromise is likely.",
                "Block malicious source addresses and devices.",
                "Restrict access using conditional access policies.",
            ],
            "Eradication": [
                "Reset the affected user's password.",
                "Remove unauthorised MFA methods and recovery information.",
                "Delete malicious forwarding rules and application permissions.",
                "Remove unauthorised devices from the account.",
            ],
            "Recovery": [
                "Restore account access after identity verification.",
                "Require secure password and MFA re-registration.",
                "Monitor the account for renewed suspicious activity.",
                "Confirm that legitimate access is functioning correctly.",
            ],
            "Post-Incident Review": [
                "Document the cause, impact, and affected resources.",
                "Review identity controls and alert effectiveness.",
                "Update conditional access and authentication policies.",
                "Record lessons learned and remediation actions.",
            ],
        },
    },
}


PHASE_OBJECTIVES: Dict[str, str] = {
    "Preparation": (
        "Establish the people, processes, tools, and controls required "
        "to respond effectively."
    ),
    "Detection and Analysis": (
        "Confirm the incident, determine its scope, and assess its impact."
    ),
    "Containment": (
        "Limit the spread and prevent additional damage while preserving evidence."
    ),
    "Eradication": (
        "Remove malicious activity, persistence, and the incident's root cause."
    ),
    "Recovery": (
        "Restore affected services safely and monitor for recurring activity."
    ),
    "Post-Incident Review": (
        "Document lessons learned and improve future security and response capability."
    ),
}


def get_supported_incident_types() -> List[str]:
    """Return all supported incident types in alphabetical order."""

    return sorted(PLAYBOOK_TEMPLATES.keys())
