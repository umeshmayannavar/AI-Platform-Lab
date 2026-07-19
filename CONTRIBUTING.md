# Contributing

Thank you for helping improve AI Platform Foundation. This repository is intentionally small and standards-focused, so contributions should keep automation, documentation, and developer workflow clear and repeatable.

## Branch naming

Use short, descriptive branch names with a type prefix:

- `feature/<short-description>` for new repository standards or workflow improvements.
- `fix/<short-description>` for corrections.
- `docs/<short-description>` for documentation-only updates.
- `chore/<short-description>` for maintenance tasks.

## Commit messages

Write commit messages in the imperative mood and keep the subject concise:

```text
Add pre-commit configuration
Improve bootstrap idempotency
Update contributor documentation
```

Group related changes into clean commits. Avoid mixing functional changes with formatting-only edits unless the formatting is required for the same change.

## Issues

Create an issue before larger changes. A useful issue includes:

- The problem or opportunity.
- The expected outcome.
- Any constraints, risks, or validation steps.
- Links to related documentation, ADRs, or pull requests.

## Pull requests

Pull requests should be focused, easy to review, and linked to an issue when one exists. Include:

- A short summary of what changed.
- The validation commands you ran.
- Screenshots only when a visible UI change is introduced.
- Notes about follow-up work, if any.

Reviewers should check that the change is scoped to the stated problem, follows repository standards, and keeps the developer workflow reproducible.

## Definition of Done

A change is done when:

- Documentation is updated for contributor-facing behavior.
- `make bootstrap` remains safe to run repeatedly.
- `make doctor` reports the expected workstation readiness checks.
- `make lint` passes for shell scripts.
- Relevant GitHub Actions checks remain green.
- The pull request explains what changed and how it was validated.

## Local validation

Run these commands before opening a pull request:

```bash
make bootstrap
make doctor
make lint
```

If pre-commit is installed, also run:

```bash
pre-commit run --all-files
```
