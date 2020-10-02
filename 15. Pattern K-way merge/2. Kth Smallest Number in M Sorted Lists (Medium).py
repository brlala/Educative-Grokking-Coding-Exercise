# Problem Statement
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

from heapq import *


def find_Kth_smallest(lists, k):
    """
    Time: O(K∗logM) going through at most K elements, M is the total number of input array
    Space: O(M)
    """
    min_heap = []

    # put the first element in the heap
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    # take the smallest(top) element and if the running count is equal to k, return the number
    number_count = number = 0
    while min_heap:
        number, i, num_list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        # if the array of the top has more elements, add next element to heap
        if len(num_list) > i + 1:
            heappush(min_heap, (num_list[i+1], i+1, num_list))
    return number


def main():
    print("Kth smallest number is: " +
    str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
main()
