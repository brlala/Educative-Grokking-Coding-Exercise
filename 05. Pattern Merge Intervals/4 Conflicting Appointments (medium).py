# Problem Statement
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

def can_attend_all_appointments(intervals):
    """
    Time: O(N+M)
    Space: O(1)
    """
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True


print(f"Can attend all appointments: {can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])}")
print(f"Can attend all appointments: {can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])}")
print(f"Can attend all appointments: {can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])}")

