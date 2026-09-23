# Changelog

## [Unreleased]

## [2.4.0] - 2026-09-23
### Added
- Transition Transparency protocol with concise user-facing Transition Briefs at meaningful Contract/Milestone boundaries.
- Explicit distinction between the human-scale Next recommended phase and agent-scale Exact next action.
- Transition execution states: `CONTINUE`, `CHECKPOINT`, and `COMPLETE`.
- Optional `next_milestone` and `next_contract` fields in `.project/WORK.json` and its schema.
- Transition-transparent conformance definition.
- `ADP.min.md`: semantically compressed machine-consumption distribution.
- `docs/MINIFIED.md`: compression contract and maintenance guidance.
- Validation for compact/full version alignment, semantic anchors, and size ceiling.

### Changed
- `STATUS.md` now owns the next recommended phase, rationale, and first action.
- `CONTINUITY.md` now distinguishes directional next-phase context from the exact cold-resume action.
- Generated `AGENTS.md` guidance reports meaningful transitions without creating routine approval gates.
- Next-work selection prioritizes dependency-ready milestone progress, important unblockers, and material risk reduction before optional polish.

## [2.3.0] - 2026-09-21
### Added
- Public open-source ADP repository.
- Universal `AGENTS.md` entrypoint.
- Repository/submodule/single-file consumption.
- Templates, schema, examples, conformance docs, validation, and CI.
### Changed
- ADP consistently expands to **Agent Development Protocol**.

## [2.2.0] - 2026-09-21
- Authorization Envelope, HIGH-autonomy continuation, work hierarchy, checkpoints, retry budgets, continuity protocol, optional WORK.json, cold-start procedure.
