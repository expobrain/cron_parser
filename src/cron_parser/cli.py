import argparse

from cron_parser.parser import parse
from cron_parser.formatter import format_cron


parser = argparse.ArgumentParser(
    description="Parse a cron expression and prints it in a human-deadable way"
)
parser.add_argument("cron_expr")


def main():
    args = parser.parse_args()

    cron_expr = parse(args.cron_expr)
    cron_formatted = format_cron(cron_expr)

    print(cron_formatted)
