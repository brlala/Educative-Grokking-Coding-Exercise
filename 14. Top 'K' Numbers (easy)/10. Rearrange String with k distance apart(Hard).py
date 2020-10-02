# Problem Statement
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

from heapq import heappop, heappush
from collections import defaultdict, deque


def reorganize_string(str, k):
    """
    Time: O(N*logN)
    Space: O(N)
    """
    if k <= 1:
        return str

    word_count = defaultdict(int)
    for char in str:
        word_count[char] += 1

    max_heap = []
    for char, frequency in word_count.items():
        heappush(max_heap, (-frequency, char))

    queue = deque()
    results = []
    while max_heap:
        frequency, char = heappop(max_heap)
        results.append(char)
        queue.append((char, frequency + 1))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(max_heap, (-frequency, char))

    return ''.join(results) if len(results) == len(str) else ''


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()