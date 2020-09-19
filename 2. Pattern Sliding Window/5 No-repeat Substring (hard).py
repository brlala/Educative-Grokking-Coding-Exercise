# Problem Statement
# Given a string, find the length of the longest substring which has no repeating characters.

def non_repeat_substring(word: str) -> int:
    """
    Time: O(n+n)
    Space: O(1)
    """
    window_start = max_length = 0
    char_index_map = {}
    for window_end in range(len(word)):
        right_char = word[window_end]
        if right_char not in char_index_map:
            char_index_map[right_char] = 0
        char_index_map[right_char] += 1

        while right_char in char_index_map and char_index_map[right_char] >= 2:
            left_char = word[window_start]
            char_index_map[left_char] -= 1
            if char_index_map[left_char] == 0:
                del char_index_map[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    print(max_length)
    return max_length


def non_repeat_substring(word: str) -> int:
    """
    Time: O(n)
    Space: O(k) k is number of distinct characters in input string
    Alternatively O(1) if we know english has only 26 characters
    """
    window_start = max_length = 0
    char_index_map = {}
    for window_end in range(len(word)):
        right_char = word[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    print(max_length)
    return max_length


def non_repeat_substring(word: str) -> int:
    """
    Leetcode top answer
    """
    used = {}
    max_length = start = 0
    for i, c in enumerate(word):
        # if seen, update index
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[c] = i

    return max_length

print(non_repeat_substring('tmmzuxt') == 5)
print(non_repeat_substring('aabccbb') == 3)
print(non_repeat_substring('abbbb') == 2)
print(non_repeat_substring('abccde') == 3)
