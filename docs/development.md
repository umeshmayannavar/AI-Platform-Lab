# Development

Use the repository `Makefile` as the primary developer interface. Commands should be safe to run repeatedly and should not require contributors to remember script paths.

## Bootstrap

Install common workstation tools with:

```bash
make bootstrap
```

The bootstrap script checks for existing tools before installing them and reports when a dependency is already available.

## Doctor

Validate local readiness with:

```bash
make doctor
```

Doctor checks required CLIs, local services such as Docker and Ollama, and expected local model availability.

## Lint

Run shell linting with:

```bash
make lint
```

The lint target runs ShellCheck against scripts in `scripts/` and `scripts/lib/`.

## Pre-commit

Install pre-commit in your preferred Python environment, then enable hooks:

```bash
python3 -m pip install pre-commit
pre-commit install
```

Run hooks across the repository with:

```bash
pre-commit run --all-files
```

The configured hooks check shell scripts, trailing whitespace, final newlines, YAML syntax, and merge conflict markers.
