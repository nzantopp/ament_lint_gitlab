# Convert Lint Report

This tool converts XML lint reports to GitLab Code Quality JSON format.

## Features

- Supports parsing `flake8` reports.
- Generates fingerprints for unique issues.
- Outputs a JSON format that is compatible with GitLab's code quality feature.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/nzantopp/ament_lint_gitlab.git
cd ament_lint_gitlab
pip install -r requirements.txt
pip install .
```
