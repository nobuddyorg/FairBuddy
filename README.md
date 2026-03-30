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
- **opengrep** - Search security relevant patterns

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

Sure! Here’s the Docker/act section rewritten as plain text with proper Markdown formatting that `mdformat` will accept:

### Docker Desktop Installation (for macOS)

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

### Running GitHub Actions Locally (act)

Once Docker Desktop is running:

- Install act:

    ```bash
    brew install act
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

Choose `medium`-Image if asked.
