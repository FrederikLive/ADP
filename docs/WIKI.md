# ADP Wiki maintenance

The files under `wiki/` are the version-controlled source for the ADP GitHub Wiki.

They are explanatory and non-normative. `ADP.md` remains canonical.

## Why keep Wiki source in the main repository?

GitHub stores a Wiki in a separate Git repository. Keeping the source here:

- makes Wiki changes reviewable beside protocol changes;
- lets repository validation catch broken local Wiki navigation;
- prevents the public Wiki from becoming an untracked second protocol;
- gives future agents a durable source from which to rebuild or sync the Wiki.

## Publishing to GitHub Wiki

GitHub documents Wikis as separate Git repositories using:

```text
https://github.com/FrederikLive/ADP.wiki.git
```

After an initial Wiki page exists on GitHub, clone the Wiki repository and copy the Markdown files from `wiki/` into its root.

Example:

```bash
git clone https://github.com/FrederikLive/ADP.wiki.git
cd ADP.wiki

# Copy the contents of the main repository's wiki/ directory here.
git add .
git commit -m "Sync ADP Wiki"
git push
```

Only the Wiki repository's default branch is rendered live by GitHub.

## Maintenance rule

Whenever a normative ADP change makes Wiki guidance stale:

1. update `ADP.md` first;
2. synchronize derived protocol artifacts;
3. update the affected `wiki/` pages;
4. run `python scripts/validate.py`;
5. publish/sync the Wiki after the main change is accepted.

Do not add normative rules only to the Wiki.
