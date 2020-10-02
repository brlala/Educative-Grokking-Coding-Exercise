# Problem Statement
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

from heapq import heappop, heappush


def find_sum_of_elements(nums, k1, k2):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)

    # remove k numbers
    for i in range(k1):
        heappop(min_heap)

    total = 0
    for i in range(k2 - k1 - 1):
        total += heappop(min_heap)
    return total


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(
        find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(
        find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()