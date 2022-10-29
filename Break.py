from datetime import timedelta
from utility import to_timedelta

"""For break creating"""


class Break:
    def __init__(self, begin: timedelta, end: timedelta, duration: int):
        self.begin = begin
        self.end = end
        self.duration = duration

    def __repr__(self):
        return f"Break: {self.begin}, {self.end}, {self.duration}"


"""Break template parsing """


class BreakTemplates:
    def __init__(self, json_di):
        self.id = json_di["id"]
        self.break_duration = json_di["break_duration"]
        self.start_time_type = json_di["start_time_type"]
        self.start_times = [to_timedelta(start_time) for start_time in json_di["start_times"]]
