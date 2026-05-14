# FairBuddy

![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)
![UV](https://img.shields.io/badge/deps-uv-purple)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![Ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)
[![CI](https://github.com/nobuddyorg/FairBuddy/actions/workflows/ci.yml/badge.svg)](https://github.com/nobuddyorg/FairBuddy/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/nobuddyorg/FairBuddy/branch/main/graph/badge.svg)](https://codecov.io/gh/nobuddyorg/FairBuddy)
![Complexipy](https://img.shields.io/badge/complexity-complexipy-black)
![OpenGrep](https://img.shields.io/badge/security-opengrep-blue)
![Zizmor](https://img.shields.io/badge/security-zizmor-blue)
![CodeQL](https://img.shields.io/badge/security-CodeQL-blue?logo=github)
![Pulumi](https://img.shields.io/badge/infrastructure-pulumi-orange?logo=pulumi)
![AWS](https://img.shields.io/badge/cloud-aws-orange?logo=amazon-aws)
![Activity](https://img.shields.io/github/last-commit/nobuddyorg/FairBuddy?logo=github)
![GitHub stars](https://img.shields.io/github/stars/nobuddyorg/FairBuddy?style=social)
[![License](https://img.shields.io/github/license/nobuddyorg/FairBuddy)](https://github.com/nobuddyorg/FairBuddy/blob/main/LICENSE)

In order install necessary dependencies, run:

```bash
./boot.sh
```

_**Note**: This bootstrap script is designed for Unix-like environments (Linux/macOS) and relies on common tools such as bash and standard CLI utilities. Supporting native Windows (e.g., PowerShell) would introduce additional maintenance overhead and platform-specific complexity. Since this bootstrap is intended for developer use only and not part of the end-user product, Linux/macOS are the primary supported environments. Windows users are encouraged to use WSL2 as a compatible execution environment._

## Run FairBuddy

Use `./buddy.sh` in CLI to gain access to all features.
With `./buddy.sh --help` you will get the complete usage overview (auto-generated).

E.g. run:

```bash
./buddy.sh test unit
```

for a unit test execution.

## Pre-commit Hooks

This project uses [prek](https://prek.j178.dev/) to enforce code quality before each commit.

### Setup

The hooks are installed automatically by `boot.sh`. To install them manually:

```bash
uv run prek install
uv run prek install --hook-type commit-msg
```

They can always be run by:

```bash
uv run prek run --all-files
```

or

```bash
./buddy test precommit
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
- **opengrep** - Search security relevant patterns

### Commit Message Format

Commit messages must follow Conventional Commits:

```text
feat: add delete_item service
fix: correct DynamoDB table name
docs: update README with setup instructions
chore: bump ruff to 0.15.1
```

## Docker Desktop Installation (for macOS)

This is required to run GitHub Actions locally with act.

You can install Docker Desktop using their own installer from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) or using HomeBrew.

- Install Docker Desktop via Homebrew Cask:

    ```bash
    brew install --cask docker
    ```

- Open Docker Desktop from `/Applications`.

    Wait until the whale icon says “Docker is running”.

- Verify installation:

    ```bash
    docker info
    docker run hello-world
    ```

## Running GitHub Actions Locally (act)

Once Docker Desktop is running:

- Install act:

    ```bash
    uv sync
    ```

- Create a `.secrets` file if your workflow uses secrets:

    ```config
    AWS_ACCESS_KEY_ID=your_aws_access_key_id_here
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key_here
    AWS_DEFAULT_REGION=your_default_region_here
    PULUMI_CONFIG_PASSPHRASE=your_pulumi_passphrase_here
    ```

- Run the Pull Request workflow:

    ```bash
    act pull_request --secret-file .secrets
    ```

    or

    ```bash
    ./buddy.sh test action
    ```

Choose `medium`-Image if asked.
