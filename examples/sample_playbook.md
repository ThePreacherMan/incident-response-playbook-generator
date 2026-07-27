# Phishing Incident Response Playbook

**Incident Type:** phishing

**Severity:** MEDIUM

## Description

Guidance for investigating, containing, and recovering from suspected phishing attacks.

## Incident Response Phases

### 1. Preparation

**Objective:** Establish the people, processes, tools, and controls required to respond effectively.

1. Maintain email security controls and anti-phishing filters.
2. Provide phishing awareness training to employees.
3. Document escalation contacts and communication procedures.
4. Ensure endpoint detection and response tools are operational.

### 2. Detection and Analysis

**Objective:** Confirm the incident, determine its scope, and assess its impact.

1. Collect the suspicious email, headers, links, and attachments.
2. Identify all recipients of the suspicious message.
3. Check whether any user clicked a link or opened an attachment.
4. Review authentication logs for suspicious sign-in activity.
5. Analyse URLs, domains, attachments, and sender infrastructure.
6. Determine whether credentials or sensitive data were exposed.

### 3. Containment

**Objective:** Limit the spread and prevent additional damage while preserving evidence.

1. Remove the phishing email from affected mailboxes.
2. Block malicious domains, URLs, senders, and file hashes.
3. Disable or restrict accounts showing signs of compromise.
4. Revoke active sessions and reset exposed credentials.
5. Isolate affected endpoints when malware execution is suspected.

### 4. Eradication

**Objective:** Remove malicious activity, persistence, and the incident's root cause.

1. Remove malicious files, browser extensions, and persistence.
2. Scan affected systems using approved security tools.
3. Delete unauthorised mailbox forwarding rules.
4. Remove malicious OAuth applications and access tokens.
5. Patch exploited software vulnerabilities where applicable.

### 5. Recovery

**Objective:** Restore affected services safely and monitor for recurring activity.

1. Restore account access after credentials are secured.
2. Monitor affected accounts and devices for recurring activity.
3. Confirm that blocked indicators remain enforced.
4. Notify affected users and provide secure access instructions.

### 6. Post-Incident Review

**Objective:** Document lessons learned and improve future security and response capability.

1. Document the incident timeline, impact, and response actions.
2. Identify security-control and awareness-training gaps.
3. Update email filtering rules and detection procedures.
4. Record lessons learned and assign remediation owners.

## Incident Documentation Checklist

- [ ] Record the date and time the incident was detected.
- [ ] Identify the person or system that reported the incident.
- [ ] Record affected users, devices, systems, and services.
- [ ] Preserve relevant logs and forensic evidence.
- [ ] Document containment and eradication actions.
- [ ] Record all internal and external communications.
- [ ] Document recovery validation results.
- [ ] Record lessons learned and remediation owners.

## Important Notice

This playbook provides general incident response guidance. Organisations should adapt the procedures to their environment, legal obligations, security policies, and escalation processes.
