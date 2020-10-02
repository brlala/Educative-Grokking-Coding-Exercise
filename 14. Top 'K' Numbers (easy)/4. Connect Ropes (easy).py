# Problem Statement
# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The
# cost of connecting two ropes is equal to the sum of their lengths.
from heapq import *


def minimum_cost_to_connect_ropes(rope_lengths):
    min_heap = []
    for length in rope_lengths:
        heappush(min_heap, length)

    result = 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)

    return result


def main():
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
