# Problem Statement
#
from heapq import heappop, heappush


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval  # interval representing employee's working hour
        # index of the list containing working hours of this employee
        self.employee_index = employee_index
        self.interval_index = interval_index  # index of the interval in the employ

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    """
    Time: O(NlgN) sort + O(lg n) poll heap
    Space: O(N) sort + O(N) min heap worst case scenario
    """
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []
    start, end = 0, 1
    # insert the first interval of each employee into the queue
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][start], i, 0))

    previous_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)
        # if previous interval not overlapping with new interval, insert a free interval
        if previous_interval.end < queue_top.interval.start:
            result.append(Interval(previous_interval.end, queue_top.interval.start))
            previous_interval = queue_top.interval
        else:  # overlapping intervals, update previous_interval if needed
            if previous_interval.end < queue_top.interval.end:
                previous_interval = queue_top.interval
        # if there are more intervals available for the same employee, add their next level interval
        employee_schedule = schedule[queue_top.employee_index]
        if len(employee_schedule) > queue_top.interval_index + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[queue_top.interval_index + 1],
                                                queue_top.employee_index,
                                                queue_top.interval_index + 1))

    return result


intervals = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(intervals):
    interval.print_interval()
    print()

intervals = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(intervals):
    interval.print_interval()
    print()
intervals = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(intervals):
    interval.print_interval()
    print()
