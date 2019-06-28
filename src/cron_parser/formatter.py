from typing import List

from cron_parser.cron import CronExpression


def format_values(values: List[int]) -> str:
    return " ".join(str(v) for v in sorted(values))


def format_cron(cron_expr: CronExpression) -> str:
    return (
        f"minute        {format_values(cron_expr.minutes)}\n"
        f"hour          {format_values(cron_expr.hours)}\n"
        f"day of month  {format_values(cron_expr.days)}\n"
        f"month         {format_values(cron_expr.months)}\n"
        f"day of week   {format_values(cron_expr.weekdays)}\n"
        f"command       {cron_expr.command}\n"
    )
