# Problem Statement
# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms
# required to hold all the meetings.

from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    """
    Time: O(NlgN) sort + O(lg n) poll heap
    Space: O(N) sort + O(N) min heap worst case scenario
    """
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    min_heap = []
    for meeting in meetings:
        # remove all meetings that have ended
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        # add the current meeting into min_heap
        heappush(min_heap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms


print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(3, 5)]) == 2)
print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]) == 2)
print(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]) == 1)
print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]) == 2)
print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]) == 2)
