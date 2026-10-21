# Using ADP

The canonical protocol is `../ADP.md`.

## Preferred: attach or mount the repository
Give the agent `https://github.com/FrederikLive/ADP`, then instruct it to read `AGENTS.md`, then apply ADP.md's reading policy: read REQUIRED material, determine CONDITIONAL applicability, and follow every applicable normative requirement before bootstrapping the target project.

## Git submodule
```bash
git submodule add https://github.com/FrederikLive/ADP.git .adp/protocol
```
Then point the target agent to `.adp/protocol/AGENTS.md` and `.adp/protocol/ADP.md`. Pin a tag/commit for reproducibility.

## Single-file mode
Copy `ADP.md` into the target root and instruct the agent to apply its reading policy: read REQUIRED material, determine CONDITIONAL applicability, and follow every applicable normative requirement.

## Recommended prompt
```text
Read the ADP repository's AGENTS.md. Apply ADP.md's reading policy: read REQUIRED material, determine CONDITIONAL applicability, and follow every applicable normative requirement.
Apply the Agent Development Protocol to this target project.
Work with HIGH autonomy inside the authorization envelope.
Do not stop for routine continue acknowledgements.
Persist continuity state so a fresh agent can resume.
```

## Optional human visualization

ADP does not require a dashboard or additional agent bookkeeping. A separate optional companion, [ADP-Observatory](https://github.com/FrederikLive/ADP-Observatory), is developing a local-first project scanner and future dashboard. For its current prototype usage, limitations, and planned one-command launcher, see the [human-facing Observatory guide](OBSERVATORY.md). This is non-normative and need not be read during routine agent work.
