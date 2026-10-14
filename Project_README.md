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
| 4    | Docker & Container Security    | ✅ Completed |
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

At the end of Week 4, pushes to `main` and pull requests targeting `main`
automatically run code checks, secret scanning, and container security checks.

```text
Developer → GitHub push / pull request → GitHub Actions
                                            │
                         ┌──────────────────┴──────────────────┐
                         ▼                                     ▼
                       test                               secret-scan
                Install dependencies                   Full-history checkout
                Flake8 → Pytest → Bandit                     Gitleaks
                         │                                     │
                         └──────────────────┬──────────────────┘
                                            │ both jobs must pass
                                            ▼
                                    container-security
                                    Build Docker image
                                    Test inside image
                                    Export image as tar
                                    Scan with Trivy
                                            │
                            HIGH / CRITICAL → Fail CI
                            No matching findings → Pass CI
```

AWS authentication, image publishing, and deployment are planned next; the
current workflow does not deploy the application.

---

# 🧠 What I Learned

Through Weeks 0–4, I learned how to connect local development, automated checks, container execution, and security gates.

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

The implemented security checks include Bandit, Gitleaks, and Trivy.

* Distinguishing package findings from exploitable application behavior
* Updating dependencies and removing unnecessary installation tooling
* Recording evidence and expiration dates for temporary exceptions
* Comparing base images using tests and vulnerability scans
* Running containers as a non-root user with restricted capabilities
* Keeping HIGH/CRITICAL security gates enabled while remediating findings

Future stages will add AWS IAM, OIDC authentication, and automated deployment.

---

# Completed Security Milestones

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

**Status: Completed.** The Flask application is containerized, runs locally,
and passes automated container tests and the HIGH/CRITICAL vulnerability gate
in GitHub Actions.

### Current Container Configuration

| Component | Current configuration |
| --- | --- |
| Base image | `python:3.12-alpine3.24` |
| OS package updates | `apk upgrade --no-cache` during the build |
| Application server | Gunicorn `26.2.0`, bound to `0.0.0.0:8000` |
| Runtime user | `appuser`, UID 1000 |
| Python dependencies | Installed from `requirements.txt`; Werkzeug `3.1.9` |
| pip | Updated to `26.2.0` for installation, then uninstalled from the final image |
| Container test settings | `--cap-drop=ALL` and `--security-opt no-new-privileges=true` |
| CI scanner | Official `aquasec/trivy:0.75.0` container |
| CI failure threshold | HIGH or CRITICAL findings, using `--exit-code 1` |
| Active vulnerability exceptions | None; the Debian-specific ignore file was removed |

The `.dockerignore` excludes Git history, local virtual environments, Python
caches, `.env` files, and macOS metadata from the build context.

The current image still includes test and lint dependencies from
`requirements.txt`. Separating development dependencies from runtime
dependencies is a future image-size and maintenance improvement.

Capability restrictions and `no-new-privileges` are container execution
settings. They are applied explicitly in CI tests and the local commands below,
and must also be configured in the future deployment environment.

### Build and Run Locally

Run these commands from the repository root with Docker Desktop running:

```bash
docker build --pull -t devsecops-app:local .

docker run --rm \
  --cap-drop=ALL \
  --security-opt no-new-privileges=true \
  devsecops-app:local \
  python -m pytest -p no:cacheprovider
```

The current test suite covers `/`, `/health`, and `/api/message` and passed
with **3 tests** during local verification.

Start the web server:

```bash
docker run -d \
  --name devsecops-local \
  --cap-drop=ALL \
  --security-opt no-new-privileges=true \
  -p 127.0.0.1:8080:8000 \
  devsecops-app:local

curl -i http://localhost:8080/health
```

Expected response: HTTP `200 OK` with `{"status":"healthy"}`. The root endpoint
at `http://localhost:8080/` returns `DevSecOps CI/CD Pipeline`.

The port mapping connects host port 8080 to container port 8000 and restricts
access to the local machine. `EXPOSE 8000` alone does not publish the port.
If host port 8080 is occupied, change the host-side number and the curl URL.
If the name `devsecops-local` already exists, inspect it with `docker ps -a`
and use a new name or remove the old container when it is no longer needed.

```bash
docker logs devsecops-local
docker stop devsecops-local
docker rm devsecops-local
```

### Scan the Image Locally

Install Trivy on macOS if it is not already installed:

```bash
brew install trivy
trivy --version
```

Inspect findings across all severities, then check the same threshold as CI:

```bash
trivy image --image-src docker --scanners vuln devsecops-app:local

trivy image --image-src docker --scanners vuln \
  --severity HIGH,CRITICAL --exit-code 1 devsecops-app:local
```

The gate returns exit code 1 when matching vulnerabilities are detected; scan
errors can also fail the command and should be checked in the logs. An
unfiltered scan is useful for reviewing LOW, MEDIUM, and UNKNOWN findings that
are not part of the CI threshold.

### Vulnerability Findings and Remediation

The initial Debian-based image used `python:3.12-slim`. Its first local scan
reported **173 package findings**: 166 OS findings and 7 Python findings.
The 44 HIGH findings represented 8 distinct CVEs, repeated across packages.

| Verification stage | Scope | Result |
| --- | --- | --- |
| Initial Debian image | All severities | 173 findings; 44 HIGH; 0 CRITICAL |
| Updated pip, Werkzeug, and liblzma5 | All severities | 170 findings; the original 9 targeted findings disappeared, but 6 pip-vendored findings were detected |
| Removed pip after dependency installation | All severities | 164 OS findings; 0 Python findings; 44 HIGH |
| Applied reviewed Debian exceptions | HIGH/CRITICAL only | 41 HIGH; 0 CRITICAL |
| Alpine comparison image, without specifying exceptions | All severities | 0 findings detected in the local scan |
| Alpine image in GitHub Actions | HIGH/CRITICAL only | Container-security job passed without an ignore file |

The remediation process included:

1. Updating Werkzeug from `3.1.8` to `3.1.9` and pip from `25.0.1` to `26.2.0`.
2. Updating Debian's `liblzma5` to a version with the available fix.
3. Investigating new findings in pip's vendored `msgpack`, `setuptools`, and
   `urllib3`; these were internal copies rather than separately installed app
   dependencies. Removing pip after installation removed these six findings
   from the subsequent report.
4. Reviewing systemd and Perl findings against the image. `systemd-homed` was
   not found in PATH or the checked system locations, and Perl could not load
   `Archive::Tar`. Temporary exceptions were documented for
   `CVE-2026-16742` and `CVE-2026-9538`, with an expiration date of November 12,
   2026. Those exceptions suppressed three package findings and are preserved
   in Git history.
5. Removing the Debian image's mount SUID bit and validating the app with
   capabilities dropped and new privilege acquisition disabled. These controls
   reduced attack opportunities but did not change the package-version scan
   results.
6. Comparing an Alpine-based image, verifying its tests, scanning it without
   Debian exceptions, and confirming the Gunicorn `/health` response before
   adopting it as the default Dockerfile.

The Alpine choice was supported by this application's observed test and scan
results. It is not a guarantee that Alpine is universally safer: it uses musl
instead of glibc, so dependencies must be checked for compatibility. Scanner
results are a snapshot of known vulnerabilities and database coverage at the
time of inspection, not proof that an image has no vulnerabilities.

### GitHub Actions Verification

On **October 13, 2026**, workflow run **#8**, at commit **`05b9229`**, passed all
three jobs on `main`:

* `test`: Flake8, Pytest, and Bandit.
* `secret-scan`: Gitleaks, with no leaks detected.
* `container-security`: Docker build, tests inside the image, image export,
  and the Trivy HIGH/CRITICAL gate.

[View the successful CI run](https://github.com/Kimmus521/devsecops_cicd_pipeline/actions/runs/38487896418)

The container job waits for both `test` and `secret-scan` using
`needs: [test, secret-scan]`. It exports the image to a tar file and mounts that
file read-only into the Trivy container. The gate remains enabled and no
vulnerability ignore file is passed to the scanner.

The successful run still reported a Node.js deprecation warning for older
actions in the `test` job and notices about an upcoming `ubuntu-latest` image
change. Action upgrades and an explicit runner OS version remain maintenance
tasks. The current local workflow selects Python 3.12; the referenced run is
historical evidence for its own committed workflow.

### Remaining Improvements Before and During Deployment

* Update the older checkout and setup-python actions in the `test` job.
* Add an automated HTTP smoke test for the Gunicorn `/health` endpoint in CI;
  the current CI container test uses Flask's test client through Pytest.
* Separate runtime dependencies from development and test tools.
* Preserve complete scan reports as CI artifacts, in addition to the gate log.
* Review immutable image/action references and an update process for them.
* Reapply and verify runtime privilege restrictions when configuring AWS.

### Reference Documentation

* [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
* [Python official image variants](https://github.com/docker-library/docs/blob/master/python/README.md)
* [Trivy image scanning](https://trivy.dev/docs/latest/guide/target/container_image/)
* [Trivy exception configuration](https://trivy.dev/docs/latest/guide/configuration/filtering/)

---

# 🚀 Next Steps

## Week 5 — AWS IAM & OIDC

Planned tasks:

* Configure GitHub Actions OIDC.
* Create a least-privilege AWS IAM role with repository and branch restrictions.
* Avoid storing long-term AWS access keys in GitHub.
* Create an Amazon ECR repository and publish images only after successful CI.

## Week 6 — Continuous Deployment

Planned AWS services:

* Amazon ECR
* Amazon ECS Fargate

The planned pipeline will deploy the image that passed CI to ECS Fargate,
verify application health, and define a rollback procedure. AWS deployment is
not implemented yet.

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
