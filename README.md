# FairBuddy

In order install necessary dependencies, run:

```bash
./boot.sh
```

## Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality before each commit.

### Setup

The hooks are installed automatically by `boot.sh`. To install them manually:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

### What Gets Checked

On every commit the following hooks run automatically:

- **Trailing whitespace** — removes trailing spaces
- **End of file** — ensures files end with a newline
- **YAML / TOML validation** — catches syntax errors in config files
- **Merge conflict markers** — prevents committing unresolved conflicts
- **Large files** — blocks accidentally committed large files
- **Ruff lint** — checks Python code and auto-fixes issues
- **Ruff format** — formats Python code
- **Commitizen** — validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)

### Commit Message Format

Commit messages must follow Conventional Commits:

```
feat: add delete_item service
fix: correct DynamoDB table name
docs: update README with setup instructions
chore: bump ruff to 0.15.1
```
