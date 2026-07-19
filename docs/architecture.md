# Architecture

AI Platform Foundation is the standards and automation layer for a portfolio of AI Platform Engineering projects. It does not implement product functionality directly; instead, it provides the repeatable repository conventions used by downstream projects.

## System context

```text
Developer Workstation
        │
        ├── Makefile targets
        ├── Bootstrap and doctor scripts
        ├── Documentation and ADRs
        └── GitHub Actions validation
                │
                ▼
AI Platform portfolio projects
        │
        ├── AI Gateway
        ├── AI Kubernetes Operations
        ├── AI Terraform Engineer
        └── AI Observability Platform
```

## Repository responsibilities

- Provide a consistent command interface through `make`.
- Validate workstation readiness with doctor checks.
- Bootstrap common developer tools without changing application behavior.
- Define documentation, contribution, linting, and CI standards.

## Non-goals

- Hosting production services.
- Managing application-specific infrastructure.
- Replacing project-specific architecture documents in downstream repositories.
