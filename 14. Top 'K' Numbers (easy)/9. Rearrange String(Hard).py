# Problem Statement
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

from heapq import heappop, heappush
from collections import defaultdict

def rearrange_string(str):
    max_heap = []
    word_count = defaultdict(int)
    for char in str:
        word_count[char] += 1

    for char, frequency in word_count.items():
        heappush(max_heap, (-frequency, char))

    previous_char, previous_frequency = None, 0
    results = []
    while max_heap:
        frequency, char = heappop(max_heap)
        if previous_char and -previous_frequency > 0:
            heappush(max_heap, (previous_frequency, previous_char))
        results.append(char)
        previous_char = char
        previous_frequency = frequency+1

    return ''.join(results) if len(results) == len(str) else ''


def main():
    print("Rearranged string: " + rearrange_string("aappp"))
    print("Rearranged string: " + rearrange_string("Programming"))
    print("Rearranged string: " + rearrange_string("aapa"))


main()