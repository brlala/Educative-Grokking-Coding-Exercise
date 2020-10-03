# Problem Statement
#

def merge(intervals_a, intervals_b):
    """
    Time: O(N+M)
    Space: O(1)
    """
    results = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]
        b_overlaps_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        # storing the intersection part
        if a_overlaps_b or b_overlaps_a:
            results.append([max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])])

        # move next from the internval which is finish first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1
    return results

print(f"Intervals intersection: {merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])}")
print(f"Intervals intersection: {merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])}")

