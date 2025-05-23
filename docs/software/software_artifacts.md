
!!! quote
    I want to gather the artifacts below as markdown documents that live and are maintained with the source code in a repository.
    Propose the best directory structure for these artifacts.
    show as directory tree
    show a directory for source code also

```
Here’s a recommended layout that keeps all your lifecycle artifacts in a docs/ tree (organized by phase), alongside your src/ code, infra, CI/CD, etc. Everything’s Markdown (or other asset) so it lives right in the repo:

project-root/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── 01-research/
│   │   └── technical-research.md
│   │
│   ├── 02-requirements/
│   │   ├── user-stories.md
│   │   ├── functional-requirements.md
│   │   ├── non-functional-requirements.md
│   │   ├── use-case-diagrams/
│   │   │   ├── login-use-case.svg
│   │   │   └── payment-use-case.svg
│   │   └── feature-backlog.md
│   │
│   ├── 03-architecture/
│   │   ├── architecture-diagrams/
│   │   │   └── system-architecture.svg
│   │   ├── ADR/
│   │   │   ├── 0001-use-postgresql.md
│   │   │   └── 0002-choose-rest.md
│   │   ├── system-design.md
│   │   └── api-specifications.md      # e.g. OpenAPI/Swagger
│   │
│   ├── 04-implementation/
│   │   ├── refactoring-plans.md
│   │   ├── legacy-refactoring.md
│   │   └── code-review-guidelines.md
│   │
│   ├── 05-testing/
│   │   ├── test-plans.md
│   │   ├── unit-tests.md
│   │   ├── integration-tests.md
│   │   ├── performance-tests.md
│   │   └── regression-testing.md
│   │
│   ├── 06-security/
│   │   ├── threat-modeling.md
│   │   ├── security-tests.md
│   │   └── audit-reports/
│   │       └── penetration-test-2025-05.pdf
│   │
│   ├── 07-deployment/
│   │   ├── deployment-scripts/        # small helpers or docs about them
│   │   ├── ci-cd-pipelines.md
│   │   └── release-notes.md
│   │
│   ├── 08-maintenance/
│   │   ├── changelog.md
│   │   ├── incidents.md
│   │   └── postmortems.md
│   │
│   └── 09-communication/
│       ├── project-plan.md
│       ├── meeting-notes/
│       │   ├── 2025-05-01-kickoff.md
│       │   └── 2025-05-15-planning.md
│       └── user-manual.md
│
├── src/                               # your application source code
│   ├── main/
│   │   └── ...  
│   ├── test/                          # automated test suites
│   │   └── ...
│   └── legacy/                        # if you need to keep “as-is” legacy code
│
├── infra/                             # IaC / Terraform / k8s manifests
│   ├── terraform/
│   └── kubernetes/
│
├── .github/
│   └── workflows/                     # GitHub Actions
│
└── scripts/                           # helper scripts (db migrations, etc.)


Why this works:

docs/01-09: keeps each phase clearly separated and numerically ordered.

subfolders for diagrams, ADRs, reports: lets you mix Markdown, images, PDFs, etc.

src/: all living code, tests, legacy folder if you must keep “old” code around.

infra/ & .github/: separate your ops/config from docs and code.

root README/CONTRIBUTING: onboarding for the whole repo.

Feel free to adjust naming or numbering to fit your team’s conventions!

```


great create the bash script to create these directories.
don't create the src sub directories


```bash
#!/usr/bin/env bash
set -e

# Create system-facing documentation directories
mkdir -p docs/system/01-research

mkdir -p docs/system/02-requirements
mkdir -p docs/system/02-requirements/use-case-diagrams

mkdir -p docs/system/03-architecture
mkdir -p docs/system/03-architecture/architecture-diagrams
mkdir -p docs/system/03-architecture/ADR
mkdir -p docs/system/04-implementation
mkdir -p docs/system/05-testing

mkdir -p docs/system/06-security
#mkdir -p docs/system/06-security/audit-reports

#mkdir -p docs/system/07-deployment
#mkdir -p docs/system/07-deployment/deployment-scripts

#mkdir -p docs/system/08-maintenance

mkdir -p docs/system/09-communication
mkdir -p docs/system/09-communication/meeting-notes

# Create user-facing documentation directory
mkdir -p docs/user

# Create other top-level directories
mkdir -p src
#mkdir -p infra/terraform
#mkdir -p infra/kubernetes
#mkdir -p .github/workflows
mkdir -p scripts

echo "Directory structure created."

```