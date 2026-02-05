from datetime import datetime, timedelta
from utils.constants import IST


def utc_now():
    return datetime.utcnow()


def utc_hours_ago(hours: int):
    return datetime.utcnow() - timedelta(hours=hours)


def to_ist(dt):
    if not dt:
        return None
    return dt.astimezone(IST)


def format_ist(dt, fmt="%Y-%m-%d %H:%M:%S"):
    if not dt:
        return "NA"
    return to_ist(dt).strftime(fmt)


def round_to_hour(dt):
    return dt.replace(minute=0, second=0, microsecond=0)
