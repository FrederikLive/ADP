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

## Updating an existing ADP project

A user can ask an ADP-aware coding agent **"Check ADP for updates"**, **"Update ADP"** or **"Migrate to ADP version X"**. These have different effects: checking is read-only; updating/migrating requires comparing trusted upstream releases to the project's actual adopted source, preserving project-specific instructions, and verifying authorized changes. Read the [ADP Project Update Guide](UPDATING_ADP.md) only when requested. This works with copied protocol files, pinned submodules, attached repositories and remote references; no new manifest or periodic network check is required.

## Human-to-agent requests

See the [optional ADP command catalogue](COMMANDS.md) for natural-language requests covering status, work, verification, handoff, updating ADP and Observatory. These are **not** new shell commands, literal reserved keywords or a required part of an ADP project. The existing project-specific `setup`, `check`, `test` and `build` command surface remains separate.

## Optional human visualization

ADP does not require a dashboard or additional agent bookkeeping. A separate optional companion, [ADP-Observatory](https://github.com/FrederikLive/ADP-Observatory), provides a development-stage scanner and offline local HTML dashboard, with a verified-installation experience still planned. For its current prototype usage, limitations, and planned one-command launcher, see the [human-facing Observatory guide](OBSERVATORY.md). This is non-normative and need not be read during routine agent work.
