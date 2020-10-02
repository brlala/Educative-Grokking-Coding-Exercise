# Problem Statement
# Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for min-heap, change this symbol for max heap
    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    """
    Time: (N∗logK)
    Space: O(N), can be O(K) if we use max heap and replace the root only if it's smaller
    """
    min_heap = []
    for point in points:
        heappush(min_heap, point)

    results = []
    for i in range(k):
        results.append(heappop(min_heap))
    return results


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

main()
