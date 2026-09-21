# AGENTS.md

## Purpose
This repository defines **ADP — Agent Development Protocol**. The canonical normative specification is [`ADP.md`](ADP.md).

## Mandatory startup
If modifying ADP: read `ADP.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, and `docs/VERSIONING.md`; inspect Git state; run `python scripts/validate.py` before completion.

If this repository is reference material for another project: read this file, then read `ADP.md` completely, apply ADP to the target project, and do not modify this repository unless explicitly asked.

## Source-of-truth hierarchy
1. `ADP.md`
2. `GOVERNANCE.md`
3. `docs/VERSIONING.md`
4. `docs/*.md`
5. `templates/` and `examples/`

If a derived artifact conflicts with `ADP.md`, `ADP.md` wins.

## Autonomy
Default autonomy is HIGH. Continue across ordinary authorized work. Stop for breaking protocol redesigns, licensing/governance changes, destructive history changes, unauthorized publication/deployment, or security-sensitive external actions.

## Definition of done
Implementation complete; validation VERIFIED; derived artifacts synchronized; version/changelog updated when required; final diff reviewed; unrelated user work preserved.
