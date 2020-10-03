# Problem Statement
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the
# second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if
# the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should
# return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
#
# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

from __future__ import annotations


class Node:
    def __init__(self, value, next: Node = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(f"{temp.value}", end='-')
            temp = temp.next
        print()


def reorder(head: Node):
    """
    Time:
    Space:
    """
    if head is None or head.next is None:
        return

    # find middle of linked list
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow is now pointing to the middle node
    head_second_half = reverse(slow)
    head_first_half = head

    # rearrange to produce the required linked list
    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    # set the next of the last Node to None
    if head_first_half is not None:
        head_first_half.next = None


def reverse(current: Node):
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    reorder(head)
    head.print_list()
