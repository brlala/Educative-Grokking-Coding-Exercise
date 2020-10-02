# Problem Statement
# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return
# the numbers in the sorted order. ‘X’ is not necessarily present in the array.


from collections import defaultdict
from heapq import heappop, heappush


class KeyCounts:
    def __init__(self, key, count):
        self.key = key
        self.count = count

    def __lt__(self, other):
        return self.count < other.count


def find_maximum_distinct_elements(nums, k):
    """
    Time: O(N) hashmap + O(n*lgn) insert into heap + O(K*lgn) extract from heap
    Space: O(N)
    """
    num_count = defaultdict(int)
    min_heap = []
    for num in nums:
        num_count[num] += 1

    distinct_count = 0
    for key, value in num_count.items():
        if value == 1:
            distinct_count += 1
        else:
            heappush(min_heap, KeyCounts(key, value))

    # remove maximum of k
    while k > 0 and min_heap:
        item = heappop(min_heap)
        k = k - item.count + 1
        if k > 0:
            distinct_count += 1

    k = max(k, 0)
    return distinct_count - k


def main():
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
