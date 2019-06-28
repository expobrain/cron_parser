from typing import List

import dataclasses

from cron_parser.exceptions import CronValueException


@dataclasses.dataclass(frozen=True)
class CronExpression:
    command: str
    minutes: List[int] = dataclasses.field(default_factory=set)
    hours: List[int] = dataclasses.field(default_factory=set)
    days: List[int] = dataclasses.field(default_factory=set)
    months: List[int] = dataclasses.field(default_factory=set)
    weekdays: List[int] = dataclasses.field(default_factory=set)

    def __post_init__(self):
        if self.minutes:
            for minute in self.minutes:
                if not (0 <= minute <= 59):
                    raise CronValueException(f"Minute range is between 0-59, got {minute})")

        if self.hours:
            for hour in self.hours:
                if not (0 <= hour <= 23):
                    raise CronValueException(f"Hour range is between 0-23, got {hour})")

        if self.days:
            for day in self.days:
                if not (1 <= day <= 31):
                    raise CronValueException(f"Day range is between 1-31, got {day})")

        if self.months:
            for month in self.months:
                if not (1 <= month <= 12):
                    raise CronValueException(f"Month range is between 1-12, got {month})")

        if self.weekdays:
            for weekday in self.weekdays:
                if not (0 <= weekday <= 6):
                    raise CronValueException(f"Weekday range is between 0-6, got {weekday})")
