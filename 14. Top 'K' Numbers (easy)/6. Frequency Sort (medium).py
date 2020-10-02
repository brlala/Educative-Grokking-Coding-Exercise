# Problem Statement
# Given a string, sort it based on the decreasing frequency of its characters.
from collections import defaultdict
from heapq import heappop, heappush


class Alphabets:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency

    def __gt__(self, other):
        return -self.frequency > -other.frequency


def sort_character_by_frequency(str):
    """
    Time: O(D∗logD)
    Space: O(N)
    """
    max_heap = []
    char_counts = defaultdict(int)
    for char in str:
        char_counts[char] += 1

    for key, value in char_counts.items():
        heappush(max_heap, Alphabets(key, value))

    result = ''
    while len(max_heap) > 0:
        item = heappop(max_heap)
        result += f"{item.char}" * item.frequency
    return result


def main():
    print("String after sorting characters by frequency: " + sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " + sort_character_by_frequency("abcbab"))


main()
