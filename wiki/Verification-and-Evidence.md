# Verification and Evidence

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP prefers executable evidence over agent confidence.

Statements such as “looks correct”, “should work”, or “probably passes” are not verification.

## Verification states

Use explicit states:

- **VERIFIED** — the check was run and passed, or equivalent evidence confirms it.
- **FAILED** — it was run and failed.
- **NOT RUN** — applicable, but not executed.
- **NOT AVAILABLE** — the required environment or dependency is unavailable.

## Evidence examples

Depending on the project:

- unit tests;
- integration tests;
- end-to-end tests;
- lint/type/format checks;
- successful build;
- runtime smoke tests;
- schema validation;
- migration verification;
- screenshots or UI automation;
- accessibility checks;
- security checks;
- performance benchmarks.

## Proportional verification

Verification should match risk.

A small isolated fix may need a targeted regression test and repository check.

A security-sensitive, migration-heavy, public-interface, or production-critical change should receive broader validation.

## Delegated verification

In delegated execution, a worker's completion claim is provisional.

The coordinator must reconcile the result with the actual Contract and evidence before project state becomes VERIFIED.

For higher-risk delegated work, rerun the relevant checks or perform an independent review.

## Definition of done

“Code written” is not done.

A substantial change is complete only when applicable acceptance criteria are satisfied, required checks are accounted for, the diff is reviewed, owned documentation reflects reality, and remaining limitations are explicit.

## Related pages

- [Core Model](Core-Model.md)
- [Delegated and Concurrent Execution](Delegated-and-Concurrent-Execution.md)
- [Continuity and Handoffs](Continuity-and-Handoffs.md)
