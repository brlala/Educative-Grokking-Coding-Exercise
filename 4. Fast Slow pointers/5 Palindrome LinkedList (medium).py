# Problem Statement
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm
# is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
from __future__ import annotations


class Node:
    def __init__(self, value, next: Node = None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Node):
    """
    Time: O(N)
    Space: O(1)
    """
    x = head
    print(f"Initial: {print_linked_list(x)}")
    if head is None or head.next is None:
        return True
    slow = fast = head
    # find middle of the linkedlist
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # reverse list
    head_second_half = reverse(slow)
    print(f"Second half head + reversed: {print_linked_list(head_second_half)}")
    print(f"Head: {print_linked_list(x)}")
    copy_head_second_half = head_second_half

    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break  # not palindrome

        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)
    print(f"Reversing back: {print_linked_list(x)}")
    if head is None or head_second_half is None:
        return True
    return False


def reverse(current: Node) -> Node:
    # stash the next pointer first, because we need to know where to go
    # previous node become the node we're sitting on
    # advance current pointer
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def print_linked_list(current: Node):
    # stash the next pointer first, because we need to know where to go
    # previous node become the node we're sitting on
    # advance current pointer
    res = []
    while current is not None:
        res.append(str(current.value))
        current = current.next
    return '-'.join(res)


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)
    print(f"LinkedList is palindromic: {is_palindromic_linked_list(head)}")

    head.next.next.next.next.next.next.next = Node(2)
    print(f"LinkedList is palindromic: {is_palindromic_linked_list(head)}")
