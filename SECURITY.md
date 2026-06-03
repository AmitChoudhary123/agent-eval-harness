# Security Policy

Agent Eval Harness is a reference evaluation tool. Benchmark data should not include secrets, personal data, customer identifiers, proprietary prompts, or confidential model outputs unless your organization has approved that use.

## Reporting issues

Open a GitHub issue for non-sensitive security concerns. For sensitive findings, contact the maintainer through the profile contact channel and avoid posting confidential benchmark data publicly.

## Security principles

- Use synthetic or anonymized benchmark data by default
- Avoid storing raw sensitive prompts or responses
- Redact customer, employee, and financial identifiers
- Treat benchmark outputs as operational evidence
- Review report artifacts before sharing externally

## Maintainer expectations

Security-related changes should explain the risk reduced and include tests when behavior changes.