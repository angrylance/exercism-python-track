from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """
    Returns a datetime after gigasecond from the given datetime moment.
    Args:
        moment(datetime): initial moment.
    Returns:
        datetime: a moment 1 gigasecond after the intial one.
    """
    return moment + timedelta(seconds=1_000_000_000)
