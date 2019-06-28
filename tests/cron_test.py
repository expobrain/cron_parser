import pytest

from cron_parser import CronExpression


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        # minute
        [{"minutes": [-1]}, "Minute range is between 0-59, got -1"],
        [{"minutes": [60]}, "Minute range is between 0-59, got 60"],
        # hour
        [{"hours": [-1]}, "Hour range is between 0-23, got -1"],
        [{"hours": [24]}, "Hour range is between 0-23, got 24"],
        # day
        [{"days": [0]}, "Day range is between 1-31, got 0"],
        [{"days": [32]}, "Day range is between 1-31, got 32"],
        # Month
        [{"months": [0]}, "Month range is between 1-12, got 0"],
        [{"months": [13]}, "Month range is between 1-12, got 13"],
        # Weekday
        [{"weekdays": [-1]}, "Weekday range is between 0-6, got -1"],
        [{"weekdays": [7]}, "Weekday range is between 0-6, got 7"],
    ],
)
def test_cron_raise_value_error(kwargs, expected):
    with pytest.raises(ValueError, match=expected):
        CronExpression(**kwargs)
