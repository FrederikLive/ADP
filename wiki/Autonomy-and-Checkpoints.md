# Autonomy and Checkpoints

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP defaults to **HIGH autonomy**. The goal is to complete the user's authorized objective without repeatedly asking for routine permission.

## Authorization Envelope

An implementation request normally authorizes reasonable, reversible, repository-local work needed to achieve the requested outcome.

Typical authorized work includes:

- reading and inspecting code;
- editing source;
- creating tests;
- fixing failures caused by the work;
- justified refactoring;
- updating owned documentation;
- running checks and builds;
- adding appropriate local tooling and CI;
- continuing to the next unblocked authorized Contract.

The Authorization Envelope does **not** silently include consequential external or destructive actions.

## Autonomy levels

- **LOW** — ask before substantial choices.
- **NORMAL** — work autonomously inside the active Contract.
- **HIGH** — continue across ordinary Contracts, Workstreams, and Milestones.
- **UNATTENDED** — continue through an authorized backlog in a suitably controlled environment.

ADP-generated projects default to **HIGH** unless the user or project requires otherwise.

## Soft checkpoint

A soft checkpoint persists state but does not normally stop execution.

Use one after meaningful transitions such as:

- Contract completion;
- architecture decisions;
- major refactors;
- migrations;
- public-interface changes;
- important verification changes;
- context pressure.

A soft checkpoint should validate, persist state, update continuity, and then continue.

## Hard checkpoint

A hard checkpoint requires human authority or information.

Typical examples:

- materially ambiguous product behavior;
- expensive-to-reverse architecture choices that cannot be safely inferred;
- destructive production/shared actions;
- history rewriting or force pushes;
- deployment or publication not already authorized;
- paid-resource provisioning;
- DNS changes;
- credential rotation;
- weakening security or privacy controls;
- missing access only the user can provide;
- repeated materially different recovery attempts failing.

## The continuation rule

Finishing a file, Atomic Unit, test, Contract, or ordinary Milestone is **not** by itself a reason to stop.

The normal loop is:

```text
implement → verify → persist → select next authorized work → continue
```

Progress reporting should not become an approval gate.

## Next

Read [Transition Transparency](Transition-Transparency.md) for how ADP keeps autonomous progress visible to the user.
