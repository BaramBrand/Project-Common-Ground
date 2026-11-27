# Agent and AI GitHub Actions Register

Last reviewed: 2026-11-27

This register distinguishes static validation/security tools from model-backed agents. Marketplace presence is not a security endorsement. Every third-party Action is pinned to an immutable commit SHA in workflow YAML.

## Added in this branch

| Action | Purpose | Authentication / cost boundary | Permissions | Decision |
|---|---|---|---|---|
| [agnix-ci](https://github.com/marketplace/actions/agnix-ci) | Validate Claude, Codex, OpenCode, MCP, skills, hooks, and related agent configuration | No model API key; downloads a pinned release binary and verifies its SHA-256 sidecar; runner minutes still apply | `contents: read` | Added as manual, non-blocking validation |
| [SecureAI-Scan](https://github.com/marketplace/actions/secureai-scan) | Static LLM, MCP, Agent Skill, and RAG risk scan | No model API key; scanner npm version pinned; runner minutes and package download apply | `contents: read`; SARIF upload disabled | Added as manual, informational scan |
| [zizmor-action](https://github.com/zizmorcore/zizmor-action) | Audit GitHub Actions workflows for dangerous patterns, permission mistakes, injection and supply-chain risks | No model API key; exact zizmor wheel version is hash-locked in the action; online audits and Advanced Security upload disabled | `contents: read` | Added as manual workflow audit |

All workflows are `workflow_dispatch` only. No workflow has been run by this integration. A configured workflow is not evidence of a successful scan.

## Reviewed agent and security candidates

| Candidate | Capability | Decision / reason |
|---|---|---|
| [Claude Code Action Official](https://github.com/marketplace/actions/claude-code-action-official) | General Claude agent for issues and PRs; can implement code changes | Defer. Requires Anthropic authentication and commonly grants write access. Only enable behind explicit provider budget, restricted tool allowlist, branch-only output and human approval. |
| [Claude Auto Code Review](https://github.com/marketplace/actions/claude-auto-code-review) | Incremental Claude PR review using read-only tools | Defer. Better risk profile than a coding agent, but still requires a Claude OAuth/API credential and consumes its quota. Small third-party action; independently audit its nested dependencies before use. |
| [Needs Human Review](https://github.com/marketplace/actions/needs-human-review) | Read-only Claude/OpenCode/Codex review with isolated file readers and shadow mode | Strong candidate for a later review-only pilot. Requires a provider key and PR/status write permissions for comments/verdict workflow. Its own documentation recommends shadow mode first. |
| [Run Gemini CLI](https://github.com/marketplace/actions/run-gemini-cli) | Gemini agent for review, triage and code tasks | Defer. Requires Google model credentials; agent write operations need separate permission design. |
| [OpenCode GitHub Action](https://github.com/marketplace/actions/opencode-github-action) | Provider-neutral coding agent runner | Defer. Provider credentials, usage limits, runner isolation and write permissions must be designed first. |
| [AgentShield](https://github.com/marketplace/actions/agentshield-security-scan) | Deep Claude/agent configuration audit: secrets, permissions, hooks, MCP, prompt injection, supply chain | High-value candidate, not installed yet. MIT, latest reviewed tag v1.6.0, but the tag object is unsigned. Do not add until release provenance and bundled action source are independently verified. Static mode needs no model key; its optional Opus pipeline does. |
| [SkillShield](https://github.com/marketplace/actions/skillshield-scan) | Scan skill bundles and saved MCP tool listings for injection and exfiltration patterns | Conditional candidate when this repo actually contains installable skill bundles. MIT, Python 3.10+, no runtime dependencies. Overlaps some SecureAI coverage. |
| [mcp-scan Action](https://github.com/marketplace/actions/mcp-scan-action) | MCP config, secrets, prompt injection, supply chain and data-flow scan | Not selected. Marketplace listing shows very small adoption; prefer better-supported, pinned scanners. Its CLI may emit public report links, which is not acceptable for private SSC without a privacy review. |
| [Agent Security Harness](https://github.com/marketplace/actions/agent-security-harness) | Multi-layer MCP/A2A and agent security testing | Research candidate only. Broad feature claims need a separate source, test-fixture and license audit before execution. |
| [Agent Assurance](https://github.com/marketplace/actions/agent-assurance) | Compare declared agent capabilities with observed permissions; policy enforcement and attestations | Research candidate. Potentially useful for enforcing least privilege, but requires policy design and attestation review before adoption. |
| [CoPirate Code Review](https://github.com/promptctl/copirate-code-review-agent) | Read-only agent PR review with Claude/Codex provider choices | Defer. Requires provider credentials and PR review write permissions; compare against Needs Human Review before selecting one. |
| [Goal-Driven AI PR Reviewer](https://github.com/marketplace/actions/goal-driven-ai-pr-reviewer) | Multi-goal isolated Claude/Codex reviews | Defer. Requires a fine-grained PAT and model credentials; avoid broad write scope. |
| [GitHub Code Agent](https://github.com/marketplace/actions/github-code-agent) | Claude/Codex from issue and PR comments | Reject for initial setup. Published configuration calls for a bot PAT with repository write and workflow permissions. |
| [Pipelock Agent Security Scan](https://github.com/marketplace/actions/pipelock-agent-security-scan) | Runtime egress control for agent/MCP/A2A traffic | Keep as an infrastructure-level candidate, not another repo scanner. Evaluate in an isolated worker design. |
| [security-actions](https://github.com/basitalisandhu/security-actions) | Composite actions for agent config, prompt secrets, SBOM diffs and license auditing | Research candidate. Promising small dependency-free actions; review each component and pin its exact commit before adding. |

## Selection rules

1. Prefer read-only analysis over code-writing agents.
2. Prefer immutable SHA pins over floating tags. Record whether the referenced commit or release is signed.
3. Keep provider-backed agents disabled until an owner-approved credential, quota, budget, maximum runtime, data scope and tool allowlist exist.
4. Never grant `contents: write`, `pull-requests: write`, `actions: write`, or `id-token: write` merely to make an agent easier to operate.
5. Do not use `workflow_run` or `pull_request_target` for untrusted PR code without a documented threat model and safe checkout controls.
6. No agent may merge, publish, release, deploy production, change secrets, alter billing, or unpause SSC execution.
7. Preserve model outputs as suggestions and require human review. Never treat an AI approval as a human approval.

## Pinned implementation references

- agnix action: `agent-sh/agnix@66c82e01f10281198449b2ab1ae125d97b3e1c2f`, release `v0.62.0`; action source commit is unsigned; release binary is checked against its SHA-256 sidecar.
- SecureAI-Scan action: `akanthed/SecureAI-Scan@5fe9187d7cf967785d4944eac805b9723265fc24`, scanner package `0.11.0`; no SARIF upload.
- zizmor action: `zizmorcore/zizmor-action@53290badfa369cb0bf7ad16342cb62c2fa47ac7b`, verified signed commit; action release `v0.8.0`; bundled zizmor `1.31.1` wheel is hash-locked.
- checkout: `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`, verified release commit `v7.0.1`.
- setup-node: `actions/setup-node@949feb2413d6458794dcd2491c4babbbce0c15c1`, verified release commit `v7.1.0`; Node 24 runtime and package-manager cache disabled.

## Activation gates

1. Verify included Actions minutes/storage and a hard $0 billing stop before dispatching any workflow.
2. Run the static checks manually and review logs before enabling any push/PR trigger.
3. Add provider credentials only through repository Actions secrets, never in files, comments, logs or artifacts.
4. For model-backed reviewers, approve provider, usage budget, maximum turns, concurrency, timeout, permitted data scope and whether comments may be posted.
5. Any generated code must arrive through a branch and pull request. No auto-merge or production deployment.

## Known limits and review notes

- SecureAI-Scan is a specialist LLM/MCP/RAG scanner, not general SAST, secrets detection, dependency auditing or runtime testing. Its documented dependency advisory check reads root `package.json` and `requirements.txt`, not lockfiles, so it does not prove the transitive dependency tree is clean.
- zizmor-action v0.8.0 is described by its maintainers as early development. The pinned action's bundled `latest` wheel is 1.31.1 while the zizmor project has published newer CLI releases; this integration pins 1.31.1 because that exact wheel is hash-locked in the action release. Revisit when the action publishes a reviewed lock for a newer CLI.
- AgentShield v1.6.0 has a useful static configuration audit and MIT license, but its reviewed tag object was unsigned. Its optional Opus mode calls Anthropic; do not enable that mode without a separate budget approval. The Action is not installed in this branch.
- The Marketplace AI-assisted category contains many pages and includes products outside repository agent execution. This is a curated high-relevance screen, not a claim that every Marketplace listing has been exhaustively audited.
