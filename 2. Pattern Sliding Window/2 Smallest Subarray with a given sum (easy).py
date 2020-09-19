import math


def smallest_subarray_with_given_sum(sum, arr):
    """
    brute force method
    Time: O(n*k)
    Space: O(1)
    """
    window_sum = 0
    min_length = math.inf
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= sum:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2)
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]) == 1)
print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]) == 3)
