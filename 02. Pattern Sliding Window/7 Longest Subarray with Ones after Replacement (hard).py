# Problem Statement
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length
# of the longest contiguous subarray having all 1s.

def non_repeat_substring(arr, k):
    """
    Time: O(n+n)
    Space: O(1)
    """
    window_start = max_ones_count = max_length = 0
    for window_end, val in enumerate(arr):
        if val == 1:
            max_ones_count += 1
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(non_repeat_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6)
print(non_repeat_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9)
