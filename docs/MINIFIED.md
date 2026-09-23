# Minified ADP Distribution

`ADP.min.md` is a **semantically compressed distribution** of ADP 2.4.0 for coding-agent contexts where token/context cost matters.

## Why semantic compression

Whitespace minification saves characters but does little to reduce language-model context use. The compact distribution removes repeated rationale, extended examples, template bodies, research discussion, and explanatory duplication while preserving operational behavior.

Current GitHub Copilot guidance recommends short, focused, self-contained repository instructions and notes that shorter instruction files are more likely to be fully processed. This supports a compact operational representation rather than a whitespace-only transform.

## Authority

`ADP.md` remains canonical and normative. `ADP.min.md` is derived. If they conflict, `ADP.md` wins.

Use the full file for ADP development, protocol interpretation/disputes, unusual/high-risk edge cases, research/rationale, and complete templates/examples.

Use the compact file for routine bootstrap, constrained context windows, repeated agent loading, local/smaller models, and successor recovery where project-local canonical docs already exist.

## Compression contract

The compact distribution must preserve at minimum:
- protocol identity/version and canonical-source warning;
- precedence/authority;
- bootstrap behavior and control plane;
- standard command surface;
- work hierarchy/contracts/evidence;
- Authorization Envelope and HIGH autonomy;
- autonomous continuation;
- Transition Transparency, Transition Briefs, and next-phase/exact-action distinction;
- soft/hard checkpoints and retry discipline;
- verification states;
- Continuity Protocol/cold start/context pressure;
- WORK.json role;
- Git/file safety;
- security/external-side-effect boundaries;
- documentation ownership;
- CI/executable enforcement;
- cross-agent portability;
- bootstrap/development loops;
- definition of done and handoff.

Repository validation checks semantic anchors and a compact/full size ceiling. Human review remains necessary after normative changes.

## Maintenance

When `ADP.md` changes normatively:
1. update `ADP.min.md` in the same change;
2. preserve the same protocol version;
3. review the compression contract;
4. run `python scripts/validate.py`;
5. compare compact/full size and review the compact diff for semantic loss.

Do not regenerate the compact file with lossy automatic summarization without review.
