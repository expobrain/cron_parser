import argparse
import sys

from cron_parser.parser import parse
from cron_parser.formatter import format_cron
from cron_parser.exceptions import CronException


parser = argparse.ArgumentParser(
    description="Parse a cron expression and prints it in a human-readable way"
)
parser.add_argument("cron_expr")


def main():
    args = parser.parse_args()

    try:
        cron_expr = parse(args.cron_expr)
    except CronException as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

    cron_formatted = format_cron(cron_expr)

    print(cron_formatted)
