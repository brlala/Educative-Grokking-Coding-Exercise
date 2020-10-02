from heapq import *


def find_Kth_smallest_number(nums, k):
    """
    use a max heap, remove the top heap if the next element is smaller
    Time: O(K*logK) insert k numebrs to heap + O((N-K)*logK) iterate through the remaining numbers
    Space: O(K)
    """
    max_heap = []

    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    return -max_heap[0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))
    # since there are two 5s in the input array, our 3rd and 4th smallest numbers s
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
