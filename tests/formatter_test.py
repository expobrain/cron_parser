import pytest
import textwrap

from cron_parser.cron import CronExpression
from cron_parser.formatter import format_cron


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        # single value
        [
            {
                "command": "/usr/bin/find",
                "minutes": set(range(0, 59, 15)),
                "hours": set([0]),
                "days": set([1]),
                "months": set(range(1, 13)),
                "weekdays": set(range(1, 6)),
            },
            # fmt:off
            textwrap.dedent("""
                minute        0 15 30 45
                hour          0
                day of month  1
                month         1 2 3 4 5 6 7 8 9 10 11 12
                day of week   1 2 3 4 5
                command       /usr/bin/find
            """),
            # fmt:on
        ]
    ],
)
def test_cron_str(kwargs, expected):
    cron_expr = CronExpression(**kwargs)
    result = format_cron(cron_expr)

    assert result.strip() == expected.strip()
