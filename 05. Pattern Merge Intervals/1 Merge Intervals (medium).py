# Problem Statement
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
# intervals.
from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print(f"[{self.start}, {self.end}]", end='')


def merge(intervals: List[Interval]):
    """
    Time: O(N) + O(NlgN) sort
    Space: O(N)
    """
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)
    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for index, itv in enumerate(intervals[1:], 1):
        if itv.start <= end:  # overlapping
            end = max(itv.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = itv.start
            end = itv.end
    merged_intervals.append(Interval(start, end))
    return merged_intervals

print(f"Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
print()
print(f"Merged intervals: ", end='')
for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
print()
print(f"Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
print()
