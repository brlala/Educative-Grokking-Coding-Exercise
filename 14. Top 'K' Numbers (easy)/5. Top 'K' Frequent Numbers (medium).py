# Problem Statement
# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
from collections import defaultdict
from heapq import heappop, heappush


def find_k_frequent_numbers(nums, k):
    """
    Time: O(N+N*logK)O(N+N∗logK)
    Space: O(N)
    """
    top_numbers = defaultdict(int)
    for num in nums:
        top_numbers[num] += 1

    min_heap = []
    for key, value in top_numbers.items():
        heappush(min_heap, (key, value))
        if len(min_heap) > k:
            heappop(min_heap)

    return [key for key, value in min_heap]


def main():
    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
