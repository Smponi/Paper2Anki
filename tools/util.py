import datetime as dt
from pathlib import Path


def get_log_name() -> Path:
    log_root = Path(__file__).parent.parent.joinpath("logs")
    today = dt.date.today()
    filename = f"{today.day:2d}-{today.month:2d}-{today.year}.log"
    return log_root.joinpath(filename)
