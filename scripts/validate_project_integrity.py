#!/usr/bin/env python3
"""Validate PCG's public governance, research and security source documents."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md", "ABOUT.md", "CHARTER.md", "GOVERNANCE.md",
    "RESEARCH-STANDARDS.md", "SECURITY.md", "ROADMAP.md", "CONTRIBUTING.md",
    "OPERATING-CAPACITY.md",
)
REQUIRED_PHRASES = {
    "README.md": ("INTELLIGENCE THROUGH COOPERATION", "independent", "Signal-Sense-Command"),
    "ABOUT.md": ("Human stewardship retains authority", "co-equal", "independent"),
    "CHARTER.md": ("Human stewardship", "independence from SSC", "Consent"),
    "GOVERNANCE.md": ("Human stewardship retains final authority", "decision records", "conflicts"),
    "RESEARCH-STANDARDS.md": ("Established", "Preliminary", "Speculative / metaphysical", "Contradicted", "Unsupported", "alternative explanations"),
    "SECURITY.md": ("Do not publish exploit details", "Never place credentials", "human review"),
    "ROADMAP.md": ("Proposed founding roadmap", "human stewardship", "intended work"),
    "CONTRIBUTING.md": ("Participation is voluntary", "Do not submit credentials", "Sources"),
    "OPERATING-CAPACITY.md": (
        "45% Signal-Sense-Command (SSC)",
        "45% Project COMMON GROUND (PCG)",
        "10% Revenue Foundry (RF)",
        "AURORA remains a research and paper-trading subsystem within SSC",
    ),
}


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            errors.append(f"missing required document: {filename}")
    for filename, phrases in REQUIRED_PHRASES.items():
        path = root / filename
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8").casefold()
        for phrase in phrases:
            if phrase.casefold() not in content:
                errors.append(f"{filename}: required governance/research phrase missing: {phrase}")
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: PCG project independence, human stewardship, research evidence, security and capacity boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
