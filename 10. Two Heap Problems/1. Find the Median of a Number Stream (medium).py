# Problem Statement
# Find the Median of a Number Stream (medium)
from heapq import *


class MedianOfAStream:
    max_heap = []  # containing first half of numbers
    min_heap = []  # containing second half of numbers

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both the heaps will have equal number of elements or max heap will have one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have even numbers, take the middle of two elements
            return (-self.max_heap[0]+self.min_heap[0])/2

        # because max heap has one more element than the mean heap
        return -self.max_heap[0]


def main():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(5)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(4)
    print("The median is: " + str(median_of_a_stream.find_median()))


main()
