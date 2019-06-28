from typing import Optional, List

import dataclasses


@dataclasses.dataclass(frozen=True)
class CronExpression:
    minutes: Optional[List[int]] = None
    hours: Optional[List[int]] = None
    days: Optional[List[int]] = None
    months: Optional[List[int]] = None
    weekdays: Optional[List[int]] = None

    def __post_init__(self):
        for minute in self.minutes or []:
            if not (0 <= minute <= 59):
                raise ValueError(f"Minute range is between 0-59, got {minute})")

        for hour in self.hours or []:
            if not (0 <= hour <= 23):
                raise ValueError(f"Hour range is between 0-23, got {hour})")

        for day in self.days or []:
            if not (1 <= day <= 31):
                raise ValueError(f"Day range is between 1-31, got {day})")

        for month in self.months or []:
            if not (1 <= month <= 12):
                raise ValueError(f"Month range is between 1-12, got {month})")

        for i, weekday in enumerate(self.weekdays or []):
            if not (0 <= weekday <= 6):
                raise ValueError(f"Weekday range is between 0-6, got {weekday})")
