# Getting Started

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is the normative protocol.

ADP can be used with a new project or added to an existing repository.

## Recommended usage

Give the coding agent access to the ADP repository and tell it to read:

1. `AGENTS.md`
2. `ADP.md`

Then describe the project you want.

A practical prompt is:

```text
Use the Agent Development Protocol from the ADP repository available in this
workspace/context.

Read its AGENTS.md and then ADP.md completely.

We are building:
<describe the project, users, constraints, and desired outcome>

Bootstrap and develop the target project according to ADP. Work with HIGH
autonomy inside the authorization envelope. Do not stop for routine
"continue" acknowledgements. Persist continuity state so another agent can
resume if your context ends.
```

## Ways to provide ADP

### Entire repository

Best when the coding harness can attach or mount another repository.

### Git submodule

```bash
git submodule add https://github.com/FrederikLive/ADP.git .adp/protocol
```

Then direct the agent to `.adp/protocol/AGENTS.md` and `.adp/protocol/ADP.md`.

### Single portable specification

Copy `ADP.md` into the project root.

### Compact distribution

Use `ADP.min.md` when context is constrained. It is a semantically compressed derivative; `ADP.md` always wins on conflict or ambiguity.

## What happens during bootstrap

An ADP agent should approximately:

1. inspect the repository before changing it;
2. understand the product, users, constraints, and acceptance criteria;
3. preserve an existing stack and conventions when appropriate;
4. establish the smallest sufficient project control plane;
5. create executable setup/check/test/build paths;
6. implement real working foundations rather than only writing documentation;
7. verify the generated project;
8. create concise agent instructions from verified reality;
9. persist status and continuity state;
10. continue automatically while authorized work remains.

## Existing repositories

ADP is not permission to rewrite a working repository into a preferred template.

For existing projects, agents should preserve established stacks, package managers, build conventions, user work, and useful project-specific instructions unless there is a justified reason to change them.

## Next

Read [Core Model](Core-Model.md) to understand how ADP represents work.
