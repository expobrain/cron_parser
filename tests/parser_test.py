import pytest

from cron_parser.cron import CronExpression
from cron_parser.exceptions import CronParseException
from cron_parser.parser import parse


@pytest.mark.parametrize(
    "cron_expr, expected",
    [
        # Invalid cron expression
        [None, "Invalid cron expression"],
        ["", "Invalid cron expression"],
        ["*", "Invalid cron expression"],
        ["* *", "Invalid cron expression"],
        ["* * *", "Invalid cron expression"],
        ["* * * *", "Invalid cron expression"],
        ["* * * * *", "Invalid cron expression"],
        # Invalid scalar values
        ["a * * * * ls", "Value 'a' is not a valid cron expression's value"],
        ["* a * * * ls", "Value 'a' is not a valid cron expression's value"],
        ["* * a * * ls", "Value 'a' is not a valid cron expression's value"],
        ["* * * a * ls", "Value 'a' is not a valid cron expression's value"],
        ["* * * * a ls", "Value 'a' is not a valid cron expression's value"],
    ],
)
def test_parse_raise_exception(cron_expr, expected):
    with pytest.raises(CronParseException, match=expected):
        parse(cron_expr)


@pytest.mark.parametrize(
    "cron_expr, expected_kwargs",
    [
        # No values
        ["* * * * * ls", {}],
        # single value
        ["0 * * * * ls", {"minutes": set([0])}],
        ["* 0 * * * ls", {"hours": set([0])}],
        ["* * 1 * * ls", {"days": set([1])}],
        ["* * * 1 * ls", {"months": set([1])}],
        ["* * * * 0 ls", {"weekdays": set([0])}],
        # multiple values
        ["0,15,30 * * * * ls", {"minutes": set([0, 15, 30])}],
        ["* 6,12 * * * ls", {"hours": set([6, 12])}],
        ["* * 1,15,20 * * ls", {"days": set([1, 15, 20])}],
        ["* * * 1,12 * ls", {"months": set([1, 12])}],
        ["* * * * 0,2,6 ls", {"weekdays": set([0, 2, 6])}],
        # duplicate values
        ["15,15,30 * * * * ls", {"minutes": set([15, 30])}],
        ["* 6,6,12 * * * ls", {"hours": set([6, 12])}],
        ["* * 1,15,15,20 * * ls", {"days": set([1, 15, 20])}],
        ["* * * 1,12,12 * ls", {"months": set([1, 12])}],
        ["* * * * 0,2,6,6 ls", {"weekdays": set([0, 2, 6])}],
        # ranged values
        ["0-4 * * * * ls", {"minutes": set([0, 1, 2, 3, 4])}],
        ["* 0-4 * * * ls", {"hours": set([0, 1, 2, 3, 4])}],
        ["* * 1-5 * * ls", {"days": set([1, 2, 3, 4, 5])}],
        ["* * * 1-5 * ls", {"months": set([1, 2, 3, 4, 5])}],
        ["* * * * 0-4 ls", {"weekdays": set([0, 1, 2, 3, 4])}],
        # Step values
        ["*/15 * * * * ls", {"minutes": set(range(0, 59, 15))}],
        ["* */12 * * * ls", {"hours": set(range(0, 23, 12))}],
        ["* * */5 * * ls", {"days": set(range(1, 31, 5))}],
        ["* * * */3 * ls", {"months": set(range(1, 12, 3))}],
        ["* * * * */2 ls", {"weekdays": set(range(0, 6, 2))}],
    ],
)
def test_parse(cron_expr, expected_kwargs):
    expected_kwargs = dict(
        {
            "minutes": set(range(0, 59 + 1)),
            "hours": set(range(0, 23 + 1)),
            "days": set(range(1, 31 + 1)),
            "months": set(range(1, 12 + 1)),
            "weekdays": set(range(0, 6 + 1)),
        },
        **expected_kwargs,
    )

    result = parse(cron_expr)
    expected = CronExpression("ls", **expected_kwargs)

    assert result == expected
