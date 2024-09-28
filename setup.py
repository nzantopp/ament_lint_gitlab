from setuptools import setup, find_packages

setup(
    name='ament_lint_gitlab',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            'convert-flake8-report=convert_flake8_report:main',  # Entry point to your script
        ],
    },
)

