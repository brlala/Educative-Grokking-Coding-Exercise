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
from collections import defaultdict, Counter


def find_permutation_in_substring(word, pattern) -> bool:
    """
    Time: O(n+n)
    Space: O(1)
    """
    res = []
    pCounter = Counter(pattern)
    sCounter = Counter(word[:len(pattern) - 1])
    for i in range(len(pattern) - 1, len(word)):
        sCounter[word[i]] += 1  # include a new char in the window
        if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
            res.append(i - len(pattern) + 1)  # append the starting index
        sCounter[word[i - len(pattern) + 1]] -= 1  # decrease the count of oldest char in the window
        if sCounter[word[i - len(pattern) + 1]] == 0:
            del sCounter[word[i - len(pattern) + 1]]  # remove the count if it is 0
    return res


def find_permutation_in_substring(word, pattern) -> bool:
    """
    Time: O(n+M)
    Space: O(M) + O(N) for results
    """
    res = []
    target = defaultdict(int)
    window = defaultdict(int)
    for x in pattern:
        target[x] += 1
    for x in word[:len(pattern) - 1]:
        window[x] += 1

    start = 0
    for end, c in enumerate(word[len(pattern) - 1:], len(pattern) - 1):
        window[c] += 1
        if window == target:
            res.append(start)
        window[word[start]] -= 1
        if window[word[start]] == 0:
            del window[word[start]]
        start += 1
    return res


print(find_permutation_in_substring('ppqp', 'pq') == [1, 2])
print(find_permutation_in_substring('abbcabc', 'abc') == [2, 3, 4])
