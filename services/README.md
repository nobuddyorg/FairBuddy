# Services

The `bom.txt` file controls which service to build, test and deploy.

## Running a Service Locally

```bash
./trigger.sh
```

## Testing a Service Locally

To run a single test:

```bash
./test.sh
```

To run all tests:

```bash
./test.sh --all
```

## Format Code

```bash
uv sync --dev
ruff check --fix
uv run ruff format .
```
