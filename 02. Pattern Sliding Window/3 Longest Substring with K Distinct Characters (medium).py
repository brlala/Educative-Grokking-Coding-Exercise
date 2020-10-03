# Problem Statement
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
def longest_substring_with_k_distinct(arr, k):
    """
    Time: O(n+n)
    Space: O(1)
    """
    window_start = 0
    max_length = 0
    char_frequency = {}
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = arr[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_substring_with_k_distinct('araaci', 2) == 4)
print(longest_substring_with_k_distinct('araaci', 1) == 2)
print(longest_substring_with_k_distinct('cbbebi', 3) == 5)
