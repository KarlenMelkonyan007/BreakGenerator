from datetime import timedelta
from Break import Break, BreakTemplates
from utility import to_timedelta


def get_breaks(break_json: BreakTemplates, class_start_time: timedelta, class_end_time: timedelta):
    breaks = []
    for begin in break_json.start_times:
        if break_json.start_time_type == "RELATIVE_TO_CLASS_START":
            breaks.append(Break(class_start_time + begin, timedelta(minutes=break_json.break_duration),
                                break_json.break_duration))
        else:
            breaks.append(Break(class_end_time - to_timedelta(begin), class_end_time - to_timedelta(begin) +
                                timedelta(minutes=break_json.break_duration), break_json.break_duration))


"""Correction of possible breaks"""


def correct_break(breaks, break_interval):
    check_interval = break_interval
    breaks.sort(key=lambda break_: break_.begin_time)
    for i in range(len(breaks) - 1):
        if breaks[i + 1].begin_time < breaks[i].end_time:
            return "Bad"
        if breaks[i + 1].begin_time - breaks[i].end_time < check_interval:
            check_interval = breaks[i + 1].begin_time - breaks[i].end_time
        if check_interval == break_interval:
            return "Good"
        return "Bad", check_interval
