# DevSecOps CI/CD Pipeline

A hands-on DevSecOps project focused on building a secure and automated CI/CD pipeline for a Python web application using GitHub Actions, security scanning tools, Docker, and AWS.

## 🎯 Project Goal

The goal of this project is to understand how security can be integrated throughout the software development and deployment lifecycle.

Rather than treating security as a final step, this project aims to build a pipeline where code quality, security testing, container security, and deployment are automated as part of CI/CD.

### Planned Pipeline

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Lint
    ├── Unit Tests
    ├── SAST
    ├── Secret Scanning
    ├── Docker Build
    ├── Container Vulnerability Scan
    ├── Push to AWS ECR
    └── Deploy to AWS
```

---

# 📅 Project Progress

| Week | Focus                          | Status      |
| ---- | ------------------------------ | ----------- |
| 0    | Environment & Repository Setup | ✅ Completed |
| 1    | Python Web Application         | ✅ Completed |
| 2    | GitHub Actions CI              | ✅ Completed |
| 3    | SAST & Secret Scanning         | ✅ Completed |
| 4    | Docker & Container Security    | ⬜ Planned   |
| 5    | AWS IAM & OIDC                 | ⬜ Planned   |
| 6    | Automated Deployment           | ⬜ Planned   |
| 7    | Documentation & Finalization   | ⬜ Planned   |

---

# Week 0 — Environment & Repository Setup

## Objectives

The first step was to prepare the development environment and establish the GitHub repository that would be used throughout the project.

### Environment

* macOS
* Python 3
* VS Code
* Git
* GitHub
* Python Virtual Environment (`.venv`)

### Repository

GitHub Repository:

`Kimmus521/devsecops_cicd_pipeline`

The repository was initialized with:

```text
devsecops_cicd_pipeline/
│
├── .gitignore
├── LICENSE
└── README.md
```

The `.gitignore` file was configured to prevent unnecessary or sensitive files from being committed.

Examples include:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

### Virtual Environment

A Python virtual environment was created to isolate project dependencies from the system Python installation.

```bash
python3 -m venv .venv
```

The environment was activated with:

```bash
source .venv/bin/activate
```

Dependencies and development tools are installed inside this environment.

---

# Week 1 — Application Development

## Objectives

Before creating a CI/CD pipeline, an application needs to exist as the target of the pipeline.

A simple Python web application was created using Flask.

The application provides a health-check endpoint and serves as the foundation for the later CI/CD and security stages.

## Project Structure

```text
devsecops_cicd_pipeline/
│
├── .github/
│   └── workflows/
│
├── tests/
│   └── test_app.py
│
├── .gitignore
├── LICENSE
├── README.md
├── app.py
└── requirements.txt
```

### `app.py`

The main application is contained in:

```text
app.py
```

The application can be run locally using Python.

The health-check endpoint provides a simple way to verify that the application is running correctly.

Example:

```text
GET /health
```

Expected response:

```json
{
    "status": "healthy"
}
```

## Dependencies

Application dependencies are documented in:

```text
requirements.txt
```

This allows the same dependencies to be installed consistently in development and later inside the CI environment.

Dependencies can be installed with:

```bash
pip install -r requirements.txt
```

---

# Unit Testing

Unit tests were created using `pytest`.

The tests are located in:

```text
tests/test_app.py
```

The purpose of the tests is to verify that important application functionality works as expected before code is integrated or deployed.

Tests can be executed locally with:

```bash
python -m pytest
```

A successful test run confirms that the application passes the current unit tests.

---

# Week 2 — GitHub Actions CI

## Objectives

The second major stage was to automate code quality checks and unit testing using GitHub Actions.

Instead of manually running tests after every code change, GitHub Actions can automatically execute the checks when code is pushed to the repository.

## CI Workflow

The workflow is located at:

```text
.github/workflows/ci.yml
```

The intended CI flow is:

```text
Git Push / Pull Request
        │
        ▼
GitHub Actions
        │
        ├── Install Dependencies
        │
        ├── Lint with Flake8
        │
        └── Run Unit Tests with Pytest
```

---

## Flake8 — Code Quality

Flake8 was added to check Python source code for style and formatting issues.

It can be run locally with:

```bash
python -m flake8 . --exclude=.venv
```

During development, Flake8 detected issues such as:

```text
W292 no newline at end of file
```

These issues were fixed before continuing with the CI pipeline.

This demonstrated the purpose of automated linting: identifying code-quality problems before code is integrated into the project.

---

## Pytest — Automated Testing

Pytest is used to execute the unit tests created during Week 1.

Local test command:

```bash
python -m pytest
```

The CI workflow runs these tests automatically after the linting stage.

The basic concept is:

```text
Code Change
    │
    ▼
Flake8
    │
    ├── Fail → Stop CI
    │
    ▼
Pytest
    │
    ├── Fail → Stop CI
    │
    ▼
CI Passed
```

This creates an initial quality gate before future security and deployment stages are added.

---

# 🔐 Current DevSecOps Architecture

At the end of Week 2, the project has established the foundation for the complete DevSecOps pipeline.

```text
                  Developer
                      │
                      ▼
              VS Code / Local
                      │
                git commit
                      │
                      ▼
               GitHub Repository
                      │
                  git push
                      │
                      ▼
              GitHub Actions
                      │
              ┌───────┴───────┐
              ▼               ▼
           Flake8           Pytest
          Code Quality       Testing
              │               │
              └───────┬───────┘
                      ▼
                 CI Result
```

---

# 🧠 What I Learned

Through the first two weeks, I learned the fundamentals of connecting local software development with Git and automated CI.

### Git & GitHub

* Creating and managing a Git repository
* Connecting a local repository to GitHub
* Working with `main` and `origin/main`
* Creating commits
* Pushing changes to GitHub
* Resolving merge conflicts
* Understanding local vs. remote repository history

### Python Development

* Creating a basic Flask application
* Managing Python dependencies with `requirements.txt`
* Using Python virtual environments
* Creating unit tests with `pytest`

### CI/CD Fundamentals

* Understanding Continuous Integration
* Automating tests after code changes
* Using GitHub Actions workflows
* Understanding jobs and steps in a workflow
* Using linting as an initial CI quality gate

### Security Mindset

The project is designed around the principle of integrating security into the development lifecycle rather than adding security only after development is complete.

Future stages will extend the pipeline with:

* SAST
* Secret scanning
* Container vulnerability scanning
* AWS IAM
* OIDC authentication
* Automated deployment

---

# 🚀 Next Steps

## Week 3 — SAST & Secret Scanning

The workflow now runs two security checks on pushes and pull requests:

* **Bandit** checks `app.py` for Python security issues after lint and tests.
  It scans application code so pytest's normal `assert` statements do not produce B101 findings.
* **Gitleaks** checks git history for accidentally committed secrets in a separate CI job.
  The checkout uses `fetch-depth: 0` to provide the commit history.

The Flask entry point was changed to a single `app.run()` without debug mode.
The `.venv_repair/` directory is ignored so local dependencies do not appear as Git changes.

Run the Python checks locally from the repository root:

```bash
python -m pip install -r requirements.txt bandit
python -m flake8 app.py tests
python -m pytest
python -m bandit app.py
```

SAST checks source code without running the application. Secret scanning checks for
credentials accidentally stored in the repository, including prior commits. A
finding needs review before treating it as a real vulnerability; do not commit a
real or example credential to test the scanner. A clean scan does not guarantee
that every vulnerability or secret has been found.

**Verification:** On September 24, 2026, both the `test` and `secret-scan` jobs
passed on `main` at commit `087fbf9`.

## Week 4 — Docker & Container Security

Planned tasks:

* Create a Dockerfile
* Containerize the Flask application
* Build the Docker image
* Scan the image with Trivy
* Introduce vulnerability-based CI gates

## Week 5 — AWS IAM & OIDC

Planned tasks:

* Configure GitHub Actions OIDC
* Create a least-privilege AWS IAM role
* Avoid storing long-term AWS access keys in GitHub

## Week 6 — Continuous Deployment

Planned AWS services:

* Amazon ECR
* Amazon ECS Fargate

The pipeline will automatically deploy the application after successful CI checks.

## Week 7 — Documentation & Finalization

Final documentation will include:

* Architecture diagram
* Complete pipeline workflow
* Security findings
* Vulnerability remediation examples
* Design decisions
* Screenshots of CI/security results

---

# 📌 Final Project Objective

The final goal is to build a complete pipeline that automatically moves code from development to secure deployment:

```text
Developer
   │
   ▼
GitHub
   │
   ▼
Lint
   │
   ▼
Unit Test
   │
   ▼
SAST
   │
   ▼
Secret Scan
   │
   ▼
Docker Build
   │
   ▼
Trivy Scan
   │
   ▼
Amazon ECR
   │
   ▼
Amazon ECS Fargate
   │
   ▼
Production
```

The project will demonstrate how **development, security, testing, and deployment can be integrated into one automated CI/CD workflow.**
