# Problem Statement
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    """
    Time: O(K∗logM) going through at most K elements, M is the total number of input array
    Space: O(M)
    """
    min_heap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # if the` sum of the two numbers from the two arrays is smaller than the s
                # element of the heap, we can 'break' here. Since the arrays are sorted i
                # descending order, we ll not be able to find a pair with a higher sum mov
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:  # we have a pair with a larger sum, remove top and insert this pai
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))
    result = []
    for (num, i, j) in min_heap:
        result.append([nums1[i], nums2[j]])
    return result


def main():
    print("Pairs with largest sum are: " + str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
