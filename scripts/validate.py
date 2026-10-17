#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
REQ=["ADP.md","ADP.min.md","AGENTS.md","README.md","LICENSE","VERSION","CHANGELOG.md","CITATION.cff","CONTRIBUTING.md","GOVERNANCE.md","SECURITY.md","CLAUDE.md","GEMINI.md",".github/copilot-instructions.md","examples/BOOTSTRAP_PROMPT.md","docs/USING_ADP.md","docs/MINIFIED.md","docs/CONFORMANCE.md","docs/COMPATIBILITY.md","docs/VERSIONING.md","docs/GLOSSARY.md","wiki/Home.md","wiki/Getting-Started.md","wiki/Conformance-and-Versioning.md","wiki/FAQ.md","schema/work.schema.json"]
errors=[]
for x in REQ:
    if not (ROOT/x).exists(): errors.append("Missing required file: "+x)
v=(ROOT/"VERSION").read_text().strip()
adp=(ROOT/"ADP.md").read_text()
if f"Version {v}" not in adp: errors.append("ADP.md version mismatch")
if "ADP means Agent Development Protocol" not in adp: errors.append("ADP identity missing")
if "Reading and conformance policy" not in adp: errors.append("ADP.md reading policy missing")
if "EXTERNAL ANALYSIS INTAKE & RECONCILIATION PROTOCOL" not in adp: errors.append("ADP.md external-analysis protocol missing")
mini=(ROOT/"ADP.min.md").read_text()
if f"version:** {v}" not in mini: errors.append("ADP.min.md version mismatch")
if "Reading and conformance policy" not in mini: errors.append("ADP.min.md reading policy missing")
if "External analysis intake and reconciliation" not in mini: errors.append("ADP.min.md external-analysis protocol missing")

# Keep public/versioned derivatives aligned with the canonical protocol version.
cff=(ROOT/"CITATION.cff").read_text()
readme=(ROOT/"README.md").read_text()
changelog=(ROOT/"CHANGELOG.md").read_text()
minified_doc=(ROOT/"docs/MINIFIED.md").read_text()
versioning=(ROOT/"docs/VERSIONING.md").read_text()
if f'version: "{v}"' not in cff: errors.append("CITATION.cff version mismatch")
if f"ADP-{v}-blue.svg" not in readme: errors.append("README protocol-version badge mismatch")
if f"## [{v}]" not in changelog: errors.append("CHANGELOG missing current version entry")
if f"ADP {v}" not in minified_doc: errors.append("docs/MINIFIED.md version mismatch")
if f"v{v}" not in versioning: errors.append("docs/VERSIONING.md recommended tag mismatch")
anchors=["Authorization Envelope","Autonomous continuation","Transition transparency","Transition Brief","Delegated and concurrent execution","Execution Brief","READ_ONLY","MUTATING","Concurrent mutation isolation","reconciliation","unlanded","Next recommended phase","Exact next action","Soft checkpoint","Hard checkpoint","VERIFIED","FAILED","NOT RUN","NOT AVAILABLE","Continuity protocol","Cold-start successor","WORK.json","Git and file safety","Security and external side effects","Definition of done","Reading and conformance policy","External analysis intake and reconciliation","PARTIALLY CONFIRMED","ALREADY RESOLVED","UNRESOLVED"]
for a in anchors:
    if a.lower() not in mini.lower(): errors.append("ADP.min.md missing semantic anchor: "+a)
ratio=len(mini.encode())/max(1,len(adp.encode()))
if ratio>0.40: errors.append(f"ADP.min.md too large: {ratio:.1%} of canonical (max 40%)")
if ratio<0.05: errors.append(f"ADP.min.md suspiciously small: {ratio:.1%} of canonical")
for p in ROOT.rglob("*.json"):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f"Invalid JSON {p}: {e}")
link=re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for p in ROOT.rglob("*.md"):
    for t in link.findall(p.read_text()):
        t=t.strip().strip("<>")
        if not t or t.startswith(("http://","https://","mailto:","#")): continue
        t=unquote(t.split("#",1)[0].split("?",1)[0])
        if t and not (p.parent/t).resolve().exists(): errors.append(f"Broken local link: {p.relative_to(ROOT)} -> {t}")
print("ADP repository validation")
print(f"Compact distribution: {len(mini.encode()):,} bytes / {len(adp.encode()):,} bytes = {ratio:.1%}")
for e in errors: print("ERROR:",e)
if errors: sys.exit(1)
print(f"VERIFIED: {len(REQ)} required files")
