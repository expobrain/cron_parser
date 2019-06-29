# Cron parser

This package provides a command line tool to parse UNIX standard [cron expressions](https://en.wikipedia.org/wiki/Cron#CRON_expression) and format them in a human-readable way.

## Installation

To install the package, from the project's directory:

```shell
pip install .
```

This installs the `parse_cron` command line utility in the system.

## Usage

To parse a cron expression:

```shell
$ parse_cron "*/15 0 1,15 * 1-5 /usr/bin/find"
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

> Note: double quotes are necessary to prevent the shell to expand the `*` character

## Tests

To run the tests install the package as editable, install the development requirements and execute the tests using [Pytest](https://docs.pytest.org/en/latest/):

```shell
pip install -e .
pip install -r requirements_dev.txt
pytest tests/
```

## Todo

- add support `JAN–DEC` and `SUN–SAT` literal values in the month and day of week fields
- tests for `parse_cron.cli:main`, using [mock](https://docs.python.org/3/library/unittest.mock.html) to simulate exceptions raised by the `parse()` function
- publish the package to Pypi
