from typing import Iterator, List
import re

from cron_parser.cron import CronExpression
from cron_parser.exceptions import CronParseException


def parse_all_values(match: re.Match, min_: int, max_: int) -> Iterator[int]:
    return range(min_, max_ + 1)


def parse_single_value(match: re.Match, min_: int, max_: int) -> List[int]:
    return [int(match.groupdict()["value"])]


def parse_range_value(match: re.Match, min_: int, max_: int) -> Iterator[int]:
    start = int(match.groupdict()["start"])
    stop = int(match.groupdict()["stop"])

    return range(start, stop + 1)


def parse_step_value(match: re.Match, min_: int, max_: int) -> Iterator[int]:
    step = int(match.groupdict()["step"])

    return range(min_, max_, step)


def parse_value_raise_exception(match: re.Match, min_: int, max_: int):
    raise CronParseException(f"Value '{match.string}' is not a valid cron expression's value")


matchers = [
    # All values
    (re.compile(r"^\*$"), parse_all_values),
    # Single value
    (re.compile(r"^(?P<value>\d+)$"), parse_single_value),
    # Values range
    (re.compile(r"^(?P<start>\d+)-(?P<stop>\d+)$"), parse_range_value),
    # Step value
    (re.compile(r"^\*/(?P<step>\d+)$"), parse_step_value),
    # Catch all regex
    (re.compile(r".*"), parse_value_raise_exception),
]


def parse_token(token: str, min_: int, max_: int) -> List[int]:
    values = []

    for value_str in token.split(","):
        for matcher, value_parse_fn in matchers:
            match = matcher.match(value_str)

            if match:
                values.extend(value_parse_fn(match, min_, max_))
                break

    return values


def parse(s: str) -> CronExpression:
    # Tokenise input string
    tokens = (s or "").strip().split(" ")

    if len(tokens) < 6:
        raise CronParseException("Invalid cron expression")

    # Parse tokens
    command = " ".join(tokens[5:])
    minutes = set(parse_token(tokens[0], 0, 59))
    hours = set(parse_token(tokens[1], 0, 23))
    days = set(parse_token(tokens[2], 1, 31))
    months = set(parse_token(tokens[3], 1, 12))
    weekdays = set(parse_token(tokens[4], 0, 6))

    # Create cron struct
    cron_expr = CronExpression(
        command, minutes=minutes, hours=hours, days=days, months=months, weekdays=weekdays
    )

    return cron_expr
