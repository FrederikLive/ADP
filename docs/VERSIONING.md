# ADP Versioning

ADP uses Semantic Versioning: `MAJOR.MINOR.PATCH`.

- MAJOR: incompatible normative protocol change.
- MINOR: backwards-compatible normative addition.
- PATCH: non-breaking clarification/correction.

Keep `VERSION`, `ADP.md`, `CHANGELOG.md`, `CITATION.cff`, and release tag aligned. Recommended tag for this release: `v2.7.1`.

Long-running target projects should pin/record the ADP version they adopted.

**Maintainer versioning vs. project adoption:** the guidance above governs releasing ADP itself. To update ADP **in a consuming project**, use the [on-demand ADP Project Update Guide](UPDATING_ADP.md). A target project's protocol pin/copy does not advance merely because GitHub `main` or upstream documentation changes. Checking for updates is read-only by default, and updates must preserve project-owned instructions and existing safety/verification obligations.

