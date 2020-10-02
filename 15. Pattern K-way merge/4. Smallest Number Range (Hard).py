# Problem Statement
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

import math
from heapq import *


def find_smallest_range(lists):
    """
    Time: O(K∗logM) going through at most K elements, M is the total number of input array
    Space: O(M)
    """
    min_heap = []
    range_start, range_end = 0, math.inf
    current_max_number = -math.inf
    # put the 1st element of each array in the max heap
    for arr in lists:
        heappush(min_heap, (arr[0], 0, arr))
        current_max_number = max(current_max_number, arr[0])
    # take the smallest(top) element form the min heap, if it gives us smaller rang
    # if the array of the top element has more elements, insert the next element in
    while len(min_heap) == len(lists):
        num, i, arr = heappop(min_heap)
        if range_end - range_start > current_max_number - num:
            range_start = num
            range_end = current_max_number

        if len(arr) > i + 1:
            # insert the next element in the heap
            heappush(min_heap, (arr[i + 1], i + 1, arr))
            current_max_number = max(current_max_number, arr[i + 1])
    return [range_start, range_end]


def main():
    print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
