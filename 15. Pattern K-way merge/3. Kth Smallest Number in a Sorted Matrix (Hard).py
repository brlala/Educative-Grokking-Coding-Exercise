# Problem Statement
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

from heapq import *


from heapq import *
def find_Kth_smallest(matrix, k):
    """
    Time: O(K∗logM) going through at most K elements, M is the total number of input array
    Space: O(M)
    """
    min_heap = []
    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(len(matrix), k)):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is e
    # if the row of the top element has more elements, add the next element to th
    number_count = number = 0
    while min_heap:
        number, i, row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(row) > i + 1:
            heappush(min_heap, (row[i+1], i+1, row))

    return number


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()