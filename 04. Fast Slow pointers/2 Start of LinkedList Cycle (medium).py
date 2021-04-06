# Problem Statement
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
from __future__ import annotations


class Node:
    def __init__(self, value, next: Node=None):
        self.value = value
        self.next = next


def has_cycle(head: Node):
    """
    Time: O(N)
    Space: O(1)
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            slow = head
            while slow != fast:
                # why this works explanation https://stackoverflow.com/a/10886319/10262825
                # Floyd's cycle algorithm
                # https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
                # https://www.youtube.com/watch?v=9YTjXqqJEFE
                slow = slow.next
                fast = fast.next
            return slow.value
    return 0


def find_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList cycle start: {has_cycle(head)}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList cycle start: {has_cycle(head)}")

    head.next.next.next.next.next.next = head
    print(f"LinkedList cycle start: {has_cycle(head)}")
