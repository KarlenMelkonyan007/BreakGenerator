from datetime import datetime, timedelta

"""String to timdelts object"""


def to_timedelta(time_str):
    time_ = datetime.strptime(time_str, "%H:%M:%S")
    return timedelta(hours=time_.hour, minutes=time_.minute, seconds=time_.second)
