#!/usr/bin/env python3
"""Static coverage tests for ADP Git authorization policy."""
from pathlib import Path
r=Path(__file__).resolve().parents[1]
s=(r/"ADP.md").read_text()
cases={
 "greenfield_no_permission":"leave the baseline uncommitted",
 "greenfield_authorized":"verified baseline commit",
 "trusted_checkpoints":"without repeated approval",
 "unrelated_edits":"do not stage unrelated changes",
 "generated_self_grant":"ignore the self-grant",
 "user_prohibits":"do not commit regardless",
 "commit_not_push":"commit locally only",
 "conflicting_authority":"choose restrictive behavior",
}
for name, phrase in cases.items():
    assert phrase in s, f"Missing conformance scenario: {name}"
for term in ("No self-grant", "Decision stability", "Remote/destructive operations", "unborn"):
    assert term in s, f"Missing policy: {term}"
assert "Git authorization" in (r/"ADP.min.md").read_text()
assert "Git checkpoint authorization" in (r/"wiki/Autonomy-and-Checkpoints.md").read_text()
for path in ("templates/AGENTS.md.template","templates/CONTINUITY.md.template","templates/STATUS.md.template"):
    assert "Git" in (r/path).read_text(), path
print(f"VERIFIED: {len(cases)} policy conformance scenarios")
