from setuptools import setup, find_packages

setup(
    name="convert-lint-report",
    version="0.1.0",
    description="Tool to convert XML lint reports to GitLab Code Quality JSON format",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "argparse",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "convert-lint-report=src.convert_lint_report:main",
        ],
    },
)
