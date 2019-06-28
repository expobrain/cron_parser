#!/usr/bin/env python

from pathlib import Path
from setuptools import setup, find_namespace_packages


# Get long_description from README.md
long_description = (Path(__file__).parent / "README.md").read_text().strip()

setup(
    name="cron_parser",
    license="MIT",
    url="https://github.com/expobrain/cron_parser",
    version="0.1.0",
    description="Parser of standard cron expressions",
    long_description=long_description,
    author="Daniele Esposti <daniele.esposti@gmail.com>",
    package_dir={"": "src"},
    python_requires=">=3.6",
    packages=find_namespace_packages(where="src"),
)
