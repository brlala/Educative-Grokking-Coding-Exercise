# Problem Statement
# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    """
    Time: O(N*logK)
    Space: O(K) main heap will only store one number at a time
    """
    min_heap = []
    # put the root of each list in the min heap
    for root in lists:
        heappush(min_heap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    result_head = result_tail = None
    while min_heap:
        smallest_node = heappop(min_heap)
        if result_head is None:
            result_head = result_tail = smallest_node
        else:
            result_tail.next = smallest_node
            result_tail = result_tail.next
        if smallest_node.next is not None:
            heappush(min_heap, smallest_node.next)
    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)
    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)
    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)
    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
