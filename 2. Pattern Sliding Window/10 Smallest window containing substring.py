# Problem Statement
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the
# given pattern.
from collections import defaultdict, Counter


def find_substring(haystack, needle):
    """
    Time: O(n+n)
    Space: O(1)
    """
    need = Counter(needle)  # hash table to store char frequency
    missing = len(needle)  # total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(haystack, 1):  # index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:  # match all chars
            while i < j and need[haystack[i]] < 0:  # remove chars to find the real start
                need[haystack[i]] += 1
                i += 1
            if end == 0 or j - i < end - start:  # update window
                start, end = i, j

            need[haystack[i]] += 1  # make sure the first appearing char satisfies need[char]>0
            missing += 1  # we missed this first char, so add missing by 1
            i += 1  # update i to start+1 for next window
    return haystack[start:end]


print(find_substring('saabdecab', 'abc') == 'cab')
print(find_substring('aabdeca', 'abc') == 'abdec')
print(find_substring('abdabca', 'abc') == 'abc')
print(find_substring('adcad', 'abc') == '')
