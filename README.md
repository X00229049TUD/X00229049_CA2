# DevOps CA2 – Python Calculator (X00229049)

## Overview

This repository contains a very small Python calculator application.

## Technologies Used

- **Language:** Python 3.11
- **Testing:** `pytest`, `pytest-cov`
- **Static Analysis:** `pylint`
- **CI/CD:** Azure DevOps Pipelines (YAML)
- **Source Control:** Git & GitHub

## Local Development Setup 

### Requirements

- Python 3.x (recommended: 3.11)
- Git
- Optional: Python virtual environment

### Setup Steps

```bash
git clone https://github.com/<ORG_NAME>/X00229049_CA2.git
cd X00229049_CA2

# (Optional) Create virtual environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Application Features

The calculator currently supports two core operations:
- add(a, b) – returns the sum of two numbers
- subtract(a, b) – returns the result of a - b

The CLI (main.py) exposes these operations as commands:
```
python main.py add <a> <b>
python main.py sub <a> <b>
```
Additional features (multiplication, division, expression evaluation, history,
etc.) will be added in later feature branches and merged through PRs.

The project follows a simple structure:
```
calculator/
    __init__.py
    core.py
tests/
    test_core.py
main.py
README.md
```

## CI Pipeline Implementation
A full CI pipeline is defined in `azure-pipelines.yml`, implemented using Azure
DevOps YAML pipelines. It performs:

### Triggers

- Runs on pushes to `main`
- Runs on PRs targeting `main`

### Pipeline Stages

1. **Set up Python environment** using local python on `self-hosted` agent.

1. **Install dependencies** -
Installs packages from `requirements.txt`.

1. **Static Analysis** -
Runs `pylint` on:
    - `calculator/`
    - `main.py`

1. **Automated Unit Tests + Coverage** - 
uses:
```
python3 -m pytest --cov=calculator --cov-report=xml:coverage.xml --cov-fail-under=80
```

This enforces a minimum coverage of 80%.

## Branch Policies and Protection
Branch protection is configured on GitHub (not Azure Repos), following CA
requirements.
### main branch protection rules
- Require pull request before merging
- Require at least 1 approving review
- Require linear history
- Block force pushes
- Block branch deletion
- Require passing status checks (Azure Pipelines) — once parallelism is granted
## Testing Strategy
- Tests live in `tests/`

- Framework: pytest

- Coverage collected with pytest-cov

- Naming convention: `test_*.py`

- Current test suite includes tests for:

    - `add(a, b)` with positive, negative, and float values

    - `subtract(a, b)` with positive, negative, and float values

- Coverage goal: ≥80%, enforced by CI.

Local test command:
```
pytest --cov=calculator
```
## Troubleshooting Guide
### Pipeline Error: “No hosted parallelism has been purchased or granted”

Occurs when Azure DevOps organization does not yet have free hosted parallelism.
## Running the App

```bash
python main.py add 2 3
python main.py sub 5 2
```