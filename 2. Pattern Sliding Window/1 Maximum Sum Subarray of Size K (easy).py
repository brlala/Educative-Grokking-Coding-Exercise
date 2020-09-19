# Problem Statement #
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
def max_sub_array_of_size_k(k, arr):
    """
    brute force method
    Time: O(n*k)
    Space: O(1)
    """
    # brute force method O(N*k)
    max_sum = 0

    for i in range(len(arr) - k):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum


def max_sub_array_of_size_k(k, arr):
    """
    removing calculating of already counted element
    Time: O(n)
    Space: O(1)
    """
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def max_sub_array_of_size_k(k, arr):
    """
    self implementation of algo above
    Time: O(n)
    Space: O(1)
    """
    if len(arr) <= k:
        return sum(arr)

    window_sum = max_sum = sum(arr[0:k])
    window_start = 0
    for window_end in range(k, len(arr)):
        window_sum -= arr[window_start]
        window_sum += arr[window_end]
        max_sum = max(max_sum, window_sum)
        window_start += 1
    return max_sum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]) == 9)
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7)
