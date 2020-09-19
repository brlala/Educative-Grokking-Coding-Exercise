# Problem Statement
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’
# letters with any letter, find the length of the longest substring having the same letters after replacement.

def length_of_longest_substring(word, replacement):
    """
    Time: O(n+n)
    Space: O(1)
    """
    count = {}
    max_repeat_letter_count = 0
    window_start = 0
    max_length = 0
    for window_end, c in enumerate(word):
        count[c] = count.get(c, 0) + 1
        max_repeat_letter_count = max(max_repeat_letter_count, count[c])

        # sliding window - repeats = replacement, if more than replacement, shift window
        if (window_end - window_start + 1 - max_repeat_letter_count) > replacement:
            count[word[window_start]] -= 1
            window_start += 1
    max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(length_of_longest_substring('aabccbb', 2) == 5)
print(length_of_longest_substring('abbcb', 1) == 4)
print(length_of_longest_substring('abccde', 1) == 3)
