#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
REQ=["ADP.md","ADP.min.md","AGENTS.md","README.md","LICENSE","VERSION","CHANGELOG.md","CONTRIBUTING.md","GOVERNANCE.md","SECURITY.md","docs/USING_ADP.md","docs/MINIFIED.md","docs/CONFORMANCE.md","docs/COMPATIBILITY.md","docs/VERSIONING.md","docs/GLOSSARY.md","schema/work.schema.json"]
errors=[]
for x in REQ:
    if not (ROOT/x).exists(): errors.append("Missing required file: "+x)
v=(ROOT/"VERSION").read_text().strip()
adp=(ROOT/"ADP.md").read_text()
if f"Version {v}" not in adp: errors.append("ADP.md version mismatch")
if "ADP means Agent Development Protocol" not in adp: errors.append("ADP identity missing")
mini=(ROOT/"ADP.min.md").read_text()
if f"version:** {v}" not in mini: errors.append("ADP.min.md version mismatch")
anchors=["Authorization Envelope","Autonomous continuation","Soft checkpoint","Hard checkpoint","VERIFIED","FAILED","NOT RUN","NOT AVAILABLE","Continuity protocol","Cold-start successor","WORK.json","Git and file safety","Security and external side effects","Definition of done"]
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
