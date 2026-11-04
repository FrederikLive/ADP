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
# Scratch-hygiene regression: Git ignores loose root files AND directories.
# This operates only inside a disposable temporary Git repository, never the user's workspace.
import shutil
import subprocess
import tempfile
if shutil.which("git") is None:
    raise AssertionError("Git executable required to validate actual ignore behavior")
with tempfile.TemporaryDirectory(prefix="adp_scratch_ignore_") as d:
    work = Path(d)
    subprocess.run(["git", "init", "-q", str(work)], check=True, capture_output=True)
    (work / ".gitignore").write_text(chr(10).join([".agent/", "/scratch_*", "/scratch-*", ""]), encoding="utf-8")
    want_ignored = (
        "scratch_probe.php",
        "scratch_d002/remote.env",
        "scratch-mysql/fixture.sql",
        ".agent/scratch/C092/probe.log",
    )
    want_visible = (
        "src/main.php",
        "config.example.php",
        "docs/work/evidence/C092/report.md",
        "directives.md",
        "worktrees/project/AGENTS.md",
    )
    for rel in want_ignored + want_visible:
        file = work / rel
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("test fixture", encoding="utf-8")
    for rel in want_ignored:
        p = subprocess.run(["git", "-C", str(work), "check-ignore", "-q", "--", rel])
        assert p.returncode == 0, f"Scratch should be ignored: {rel}"
    for rel in want_visible:
        p = subprocess.run(["git", "-C", str(work), "check-ignore", "-q", "--", rel])
        assert p.returncode == 1, f"Source should remain visible: {rel}"

for name, phrase in (
    ("canonical workspace hygiene", "# 15. Local agent workspace state and scratch hygiene"),
    ("file and directory ignore", "/scratch_*"),
    ("canonical scratch path", ".agent/scratch/<contract-id>/<purpose>/"),
    ("conditional classification", "PRIVATE_SECRET"),
    ("destructive-clean guard", "git clean -fdx"),
):
    assert phrase in (r / "ADP.md").read_text(), name
print(f"VERIFIED: {len(cases)} policy conformance scenarios + scratch ignore/file-safety regression")
