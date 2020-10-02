# Problem Statement
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
from collections import defaultdict
from heapq import heappush, heappop


class Element:
    def __init__(self, number, frequency, sequence_number):
        self.number = number
        self.frequency = frequency
        self.sequence_number = sequence_number

    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return -self.frequency < -other.frequency
        # if both elements have same frequency, return the element that was pushed last
        return self.sequence_number > other.sequence_number


class FrequencyStack:
    sequence_number = 0
    max_heap = []
    frequency_map = defaultdict(int)

    def push(self, num):
        self.frequency_map[num] += 1
        heappush(self.max_heap, Element(num, self.frequency_map[num], self.sequence_number))
        self.sequence_number += 1

    def pop(self):
        num = heappop(self.max_heap).number
        # decrement the frequency or remove if this is the last number
        if self.frequency_map[num] > 1:
            self.frequency_map[num] -= 1
        else:
            del self.frequency_map[num]
        return num


def main():
    frequency_stack = FrequencyStack()
    frequency_stack.push(1)
    frequency_stack.push(2)
    frequency_stack.push(3)
    frequency_stack.push(2)
    frequency_stack.push(1)
    frequency_stack.push(2)
    frequency_stack.push(5)
    print(frequency_stack.pop())


main()
