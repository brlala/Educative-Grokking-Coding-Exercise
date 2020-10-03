# Problem Statement
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
#
# If the total number of nodes in the LinkedList is even, return the second middle node.
from __future__ import annotations


class Node:
    def __init__(self, value, next: Node = None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head: Node):
    """
    Time: O(N)
    Space: O(1)
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow.value


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(f"LinkedList has middle: {find_middle_of_linked_list(head)}")

    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has middle: {find_middle_of_linked_list(head)}")

    head.next.next.next.next.next = Node(7)
    print(f"LinkedList has middle: {find_middle_of_linked_list(head)}")
