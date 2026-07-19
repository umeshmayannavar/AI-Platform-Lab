# Platform Foundation

> Foundation repository for building production-grade AI Platform Engineering projects.

---

## Vision

This repository establishes the engineering standards, project structure, documentation practices, automation, and development environment used across all AI Platform Engineering projects in this portfolio.

Rather than building isolated demos, the objective is to build a cohesive platform that demonstrates real-world engineering practices used to deploy, operate, and maintain AI systems.

---

## Goals

- Build production-quality AI Platform projects
- Follow Platform Engineering best practices
- Emphasize reproducibility and automation
- Document architecture and design decisions
- Maintain consistent project standards

---

## Repository Structure

```text
docs/                  Documentation, architecture notes, and ADRs
scripts/               Bootstrap, doctor, and shared shell helpers
.github/workflows/     Continuous integration checks
Makefile               Primary developer command interface
CONTRIBUTING.md        Contribution standards and review expectations
```

---

## Quick Start

Use the `Makefile` as the primary interface for local development.

### Bootstrap developer tools

```bash
make bootstrap
```

The bootstrap command installs common CLI tools with Homebrew. It is designed to be safe to run repeatedly and reports tools that are already installed.

### Run platform doctor

```bash
make doctor
```

Doctor validates required command-line tools, local services, and expected local model availability.

### Run lint checks

```bash
make lint
```

Lint runs ShellCheck against repository shell scripts.

### Install pre-commit

Install pre-commit in your preferred Python environment:

```bash
python3 -m pip install pre-commit
```

### Enable git hooks

After installing pre-commit, enable the repository hooks:

```bash
pre-commit install
```

Run all hooks manually with:

```bash
pre-commit run --all-files
```

The configured hooks check shell scripts, trailing whitespace, final newlines, YAML syntax, and merge conflict markers.

---

## Documentation

Start with:

- [Documentation index](docs/README.md)
- [Architecture overview](docs/architecture.md)
- [Development workflow](docs/development.md)
- [Contributing guide](CONTRIBUTING.md)

---

## Roadmap

This repository serves as the foundation for upcoming projects including:

- AI Gateway
- AI Kubernetes Operations
- AI Terraform Engineer
- AI RAG Platform
- AIOps Platform
- AI Observability Platform

---

## Engineering Principles

- Architecture before implementation
- Documentation before optimization
- Automation over manual work
- Simplicity over unnecessary complexity
- Reproducibility by default
