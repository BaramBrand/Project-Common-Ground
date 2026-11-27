# Agent and AI GitHub Actions Register

Last reviewed: 2026-11-27

This register separates installed static checks from optional agent runners. Marketplace presence is not a security endorsement.

## Added in this branch

| Action | Purpose | Authentication / cost | Permissions | Decision |
|---|---|---|---|---|
| [agnix-ci](https://github.com/marketplace/actions/agnix-ci) | Validate Claude, Codex, OpenCode, MCP, skills, hooks, and other agent configuration | No model API key; downloads a pinned release binary with SHA-256 sidecar verification | `contents: read` | Added as manual, non-blocking validation |
| [SecureAI-Scan](https://github.com/marketplace/actions/secureai-scan) | Static AI/LLM, MCP, Agent Skill, and RAG security scan | No model API key; pinned scanner version; runner time still consumes GitHub Actions quota | `contents: read`; SARIF upload disabled | Added as manual, informational scan |

Both workflows use `workflow_dispatch` only. They do not run on pushes or pull requests. They are not evidence of a successful scan until a run is explicitly started and its logs are reviewed.

## Reviewed but not enabled

| Action | Capability | Why it is not enabled yet |
|---|---|---|
| [Claude Code Action Official](https://github.com/marketplace/actions/claude-code-action-official) | Claude can answer issues, review PRs, and implement changes | Requires Anthropic/provider authentication and normally uses repository write permissions. Needs an owner-approved permission and usage budget design. |
| [Claude Auto Code Review](https://github.com/marketplace/actions/claude-auto-code-review) | Read-only Claude PR review with inline comments | Requires a Claude OAuth token or API key and consumes the associated plan/API allowance. Small third-party project with a limited public maintenance history; nested actions also need independent pinning review. |
| [Run Gemini CLI](https://github.com/marketplace/actions/run-gemini-cli) | Gemini CLI agent for PR review, triage, and code work | Requires Google model authentication; no credential or usage budget is configured here. |
| [OpenCode GitHub Action](https://github.com/marketplace/actions/opencode-github-action) | Run OpenCode with a selected model/provider in CI | Provider-specific credentials and model billing/quota controls are required. |
| [GitHub Code Agent](https://github.com/marketplace/actions/github-code-agent) | Invoke Claude or Codex from issue/PR comments | Its published setup calls for a bot PAT with repository write and workflow permissions. Excessive privilege for initial integration. |
| [Pipelock Agent Security Scan](https://github.com/marketplace/actions/pipelock-agent-security-scan) | Agent network egress, MCP/A2A traffic, and prompt-injection defense | Runtime proxy/security layer, not a substitute for repo CI. Evaluate in an isolated test environment before adoption. |

## Activation gates

1. Verify GitHub Actions included minutes, storage, and any hard $0 billing limit before running hosted workflows.
2. Add provider credentials only through repository Actions secrets, never in files, comments, or logs.
3. Approve the provider, subscription/API cost boundary, maximum turns, concurrency, timeout, and permitted data scope.
4. Keep agent runners read-only unless a separate reviewed design authorizes a narrowly scoped write operation.
5. Any generated change must arrive through a branch and pull request. No agent may merge or production-deploy.

## Pinned implementation references

- agnix action source: `agent-sh/agnix@66c82e01f10281198449b2ab1ae125d97b3e1c2f`, release `v0.62.0`.
- SecureAI-Scan action source: `akanthed/SecureAI-Scan@5fe9187d7cf967785d4944eac805b9723265fc24`, scanner package `0.11.0`.
- GitHub checkout: `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`.
- Node setup: `actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020`.

The agnix release tag is unsigned; the action pins its source commit and verifies the downloaded binary against the release's SHA-256 sidecar. SecureAI-Scan's Marketplace page and its tagged action metadata were checked; the workflow explicitly disables the action's SARIF-upload step. These controls reduce drift and permissions but do not replace independent source review.

## PCG scope
PCG is currently a public research and governance repository. Keep agent outputs factual, privacy-preserving, and clearly labeled. The informational scan does not certify the research, governance, or website.
