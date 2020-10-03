# Problem Statement
#
from heapq import heappop, heappush


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    """
    Time: O(NlgN) sort + O(lg n) poll heap
    Space: O(N) sort + O(N) min heap worst case scenario
    """
    jobs.sort(key=lambda x: x.start)
    max_cpu_load = current_cpu_load = 0
    min_heap = []
    for job in jobs:
        # remove all jobs that have ended
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
        # add the current job into min_heap
        heappush(min_heap, job)
        current_cpu_load += job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load


print(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]) == 7)
print(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]) == 15)
print(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]) == 8)
