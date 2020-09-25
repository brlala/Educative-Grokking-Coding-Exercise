# Problem Statement
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head, k):
    """
    Time:
    Space:
    """
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the linked list, current will be the last node
        last_node_of_sub_list = current
        next = None

        i = 0
        # reverse the nodes between 'p' and 'q'
        while current is not None and i < k:  # revere 'k' nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the first part
        if last_node_of_previous_part is not None:
            # 'previous' is now the first node of the sub-list
            last_node_of_previous_part.next = previous
        # this means p == 1 i.e. we are changing the first node (head) of the linkedlist
        else:
            head = previous

        # connect with the last part
        last_node_of_sub_list.next = current

        # skip 'k' nodes
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1

        if current is None:
            break
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_alternate_k_elements(head, 2)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()
