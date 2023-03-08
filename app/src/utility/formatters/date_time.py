from datetime import datetime, timezone


def datetime_2_isoformat(date_time: datetime) -> str:
    return date_time.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
