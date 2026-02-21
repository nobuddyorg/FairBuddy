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

### What Gets Checked

On every commit the following hooks run automatically:

- **Trailing whitespace** — removes trailing spaces
- **End of file** — ensures files end with a newline
- **Mixed line endings** — prevents inconsistent LF/CRLF usage
- **YAML / TOML / JSON / XML validation** — catches syntax errors in config and data files
- **Merge conflict markers** — prevents committing unresolved conflicts
- **Case conflicts** — prevents files that differ only by letter case
- **Executable files with shebangs** — ensures executables define an interpreter
- **Private key detection** — prevents accidentally committing private keys
- **Large files** — blocks accidentally committed large files
- **Protected branches** — prevents commits to restricted branches (if configured)
- **Ruff lint** — checks Python code and auto-fixes issues
- **Ruff format** — formats Python code
- **Commitizen** — validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)

### Commit Message Format

Commit messages must follow Conventional Commits:

```text
feat: add delete_item service
fix: correct DynamoDB table name
docs: update README with setup instructions
chore: bump ruff to 0.15.1
```
