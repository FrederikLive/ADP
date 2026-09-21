#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
REQ=["ADP.md","AGENTS.md","README.md","LICENSE","VERSION","CHANGELOG.md","CONTRIBUTING.md","GOVERNANCE.md","SECURITY.md","docs/USING_ADP.md","docs/CONFORMANCE.md","docs/COMPATIBILITY.md","docs/VERSIONING.md","docs/GLOSSARY.md","schema/work.schema.json"]
errors=[]
for x in REQ:
    if not (ROOT/x).exists(): errors.append("Missing required file: "+x)
v=(ROOT/"VERSION").read_text().strip()
adp=(ROOT/"ADP.md").read_text()
if f"Version {v}" not in adp: errors.append("ADP.md version mismatch")
if "ADP means Agent Development Protocol" not in adp: errors.append("ADP identity missing")
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
for e in errors: print("ERROR:",e)
if errors: sys.exit(1)
print(f"VERIFIED: {len(REQ)} required files")
