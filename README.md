# FairBuddy

In order install necessary dependencies, run:

```bash
./boot.sh
```

## Pre-commit Hooks

This project uses [prek](https://prek.j178.dev/) to enforce code quality before each commit.

### Setup

The hooks are installed automatically by `boot.sh`. To install them manually:

```bash
prek install
prek install --hook-type commit-msg
```

They can always be run by:

```bash
prek run --all-files
```

The same check is done remotely during PullRequest action runs.

### What Gets Checked

On every commit the following hooks run automatically:

- **Standard Hygiene Tasks** - line endings, whitespaces, ...
- **Ruff lint** - checks Python code and auto-fixes issues
- **Ruff format** - formats Python code
- **Commitizen** - validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
- **PyProject validation** - by validating the toml file
- **MD Format** - formats markdown files
- **MD Linting** - opinionated markdown formatting
- **typos** - detecting typos in code and fixing them
- **shellcheck** - checking shell scripts
- **zizmor** - linting GitHub actions
- **ty**- Python type checker
- **complexipy** - Python checker for cognitive complexity

### Commit Message Format

Commit messages must follow Conventional Commits:

```text
feat: add delete_item service
fix: correct DynamoDB table name
docs: update README with setup instructions
chore: bump ruff to 0.15.1
```

## Unit Testing

Unit tests are run by:

```bash
uv run pytest -m "not integration"
```

You can include integration tests by reducing to:

```bash
uv run pytest
```

And run it including code coverage with:

```bash
uv run pytest -m "not integration" --junitxml=reports/test-results.xml --cov=services --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-report=html:reports/htmlcov --cov-fail-under=80
```
