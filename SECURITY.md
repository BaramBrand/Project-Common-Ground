# Security Policy

Project COMMON GROUND takes the confidentiality, integrity and availability of its public repository, website, research materials and contributor information seriously.

## Scope
This policy covers security vulnerabilities affecting:
- The PCG public website and repository.
- Project-controlled source code, documentation, build workflows and configuration.
- Project-controlled integrations or data stores, if introduced later.

It does not authorize testing of third-party systems, accounts, infrastructure or services.

## Reporting a vulnerability
- Do not publish exploit details, credentials, personal data or proof-of-concept material in a public issue.
- If GitHub private vulnerability reporting is enabled for this repository, use that private reporting channel.
- If private reporting is unavailable, contact the repository owner through the contact method on the owner's GitHub profile and request a private security-reporting route.
- Include the affected component, impact, reproduction conditions, relevant versions or commits, and a safe way to coordinate remediation.
- Do not include real secrets or another person's personal information in the report.

## Handling and disclosure
- Reports will be assessed and acknowledged as project capacity permits; no response-time or remediation guarantee is implied.
- The project will seek to validate reports, minimize access to submitted details, coordinate a fix and publish an appropriately redacted advisory when disclosure is justified.
- Do not publicly disclose an unremediated vulnerability without reasonable coordination, except where immediate disclosure is necessary to prevent serious harm.
- Reporters should avoid destructive testing, data access beyond what is necessary to demonstrate impact, denial-of-service activity or persistence.

## Project security practices
As capabilities are introduced, PCG intends to apply:
- Least-privilege access and scoped credentials.
- Secret minimization and rotation.
- Dependency and workflow review.
- Protected changes, provenance and backups.
- Data minimization, retention limits and documented deletion.
- Accessible correction and incident-reporting procedures.
- Human review before publication, access changes or consequential actions.

These are intended practices, not a claim that every control has already been implemented or independently audited.

## Privacy boundary
Never place credentials, private correspondence, medical records, financial account data or sensitive personal information in public repository issues, commits or pull requests. Use private channels and disclose only what is necessary.

## Status and limitations
PCG is an early-stage project. This policy does not represent a certification, independent security audit, formal incident-response service or guaranteed support commitment.
