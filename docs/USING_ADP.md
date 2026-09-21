# Using ADP

The canonical protocol is `../ADP.md`.

## Preferred: attach or mount the repository
Give the agent `https://github.com/FrederikLive/ADP`, then instruct it to read `AGENTS.md` and `ADP.md` completely before bootstrapping the target project.

## Git submodule
```bash
git submodule add https://github.com/FrederikLive/ADP.git .adp/protocol
```
Then point the target agent to `.adp/protocol/AGENTS.md` and `.adp/protocol/ADP.md`. Pin a tag/commit for reproducibility.

## Single-file mode
Copy `ADP.md` into the target root and instruct the agent to read it completely.

## Recommended prompt
```text
Read the ADP repository's AGENTS.md and then ADP.md completely.
Apply the Agent Development Protocol to this target project.
Work with HIGH autonomy inside the authorization envelope.
Do not stop for routine continue acknowledgements.
Persist continuity state so a fresh agent can resume.
```
