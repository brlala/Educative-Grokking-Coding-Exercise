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


def rotate(head, rotations):
    """
    Time:
    Space:
    """
    if head is None or head.next is None or rotations <= 0:
        return head

    start_of_node_list = head

    list_length = 1
    # get to the end of list
    while head.next != None:
        head = head.next
        list_length += 1

    end_of_node_list = head
    rotations %= list_length  # no need to do rotations more than the length of the list
    end_of_node_list.next = start_of_node_list
    i = 0
    while i < rotations:
        end_of_node_list = end_of_node_list.next
        i += 1

    next = end_of_node_list.next
    end_of_node_list.next = None

    return next


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
result = rotate(head, 9)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()
