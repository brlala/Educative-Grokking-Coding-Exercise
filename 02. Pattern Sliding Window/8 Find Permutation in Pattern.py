# Problem Statement
# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six
# permutations:
#
# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.
from collections import defaultdict


def find_permutation_in_substring(word, pattern) -> bool:
    """
    Time: O(n+n)
    Space: O(1)
    """
    A = [ord(x) - ord('a') for x in pattern]
    B = [ord(x) - ord('a') for x in word]

    target = [0] * 26
    for x in A:
        target[x] += 1

    window = [0] * 26
    for i, x in enumerate(B):
        # sliding window
        window[x] += 1
        if i >= len(A):
            window[B[i - len(A)]] -= 1
        if window == target:
            return True
    return False


print(find_permutation_in_substring('oidbcaf', 'abc') is True)
print(find_permutation_in_substring('bcdxabcdy', 'bcdyabcdx') is True)
print(find_permutation_in_substring('aaacb', 'abc') is True)
print(find_permutation_in_substring('odicf', 'dc') is False)
