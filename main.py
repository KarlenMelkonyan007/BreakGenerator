import itertools
import json
from functions import get_breaks, correct_break
from Break import BreakTemplates
from utility import to_timedelta


def answer(break_products, break_interval):
    res = []
    check_intervals = []

    for break_ in break_products:
        ans = correct_break(break_, break_interval)
        if type(ans) is str:
            if ans == "Good":
                res.append(break_)
            check_intervals.append(ans[1])
    if res:
        return res, break_interval
    if check_intervals:
        break_interval = max(check_intervals)
        return answer(break_products, break_interval)
    return []


def main():
    span_id = input('')
    class_begin = to_timedelta(input(''))
    class_end = to_timedelta((input('')))
    break_interval = to_timedelta("2:00:00")
    with open("data.json", "r") as js_file:
        js = json.load(js_file)

    id_info = js[span_id]
    breaks = [BreakTemplates(i) for i in id_info]
    all_breaks = [get_breaks(break_info, class_begin, class_end) for break_info in breaks]
    break_products = itertools.product(all_breaks)
    res = answer(break_products, break_interval)
    return res




