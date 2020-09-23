# Problem Statement
# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct
# position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

def insert(intervals, new_interval):
    """
    Time:
    Space:
    """
    merged = []
    i, start, end = 0, 0, 1
    # skip (and add to output) all intervals that come before the new interval
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merged all intervals that overlap with new_interval
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    merged.append(new_interval)

    # add all remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


print(f"Intervals after inserting new interval: {insert([[1, 3], [5, 7], [8, 12]], [4, 6])}")
print(f"Intervals after inserting new interval: {insert([[1, 3], [5, 7], [8, 12]], [4, 10])}")
print(f"Intervals after inserting new interval: {insert([[2, 3], [5, 7]], [1, 4])}")
