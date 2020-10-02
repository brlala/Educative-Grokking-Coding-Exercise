from heapq import *


def find_k_largest_numbers(nums, k):
    """
    Time: O(K*logK) insert k numbers to heap + O((N-K)*logK) iterate through the remaining numbers
    Space: O(K)
    """
    result = []

    for i in range(k):
        heappush(result, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > result[0]:
            heappop(result)
            heappush(result, nums[i])
    return result


def main():
    print("Here are the top K numbers: " + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
    print("Here are the top K numbers: " + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
