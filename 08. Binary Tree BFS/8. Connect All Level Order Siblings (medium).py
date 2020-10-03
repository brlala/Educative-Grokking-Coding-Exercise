# Problem Statement
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root: TreeNode):
    """
    This method is written by me, more like functional programming
    Time: O(N)
    Space: O(N)
    """
    if root is None:
        return

    queue = deque()
    queue.append(root)
    all_nodes = []
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            all_nodes.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    for i in range(len(all_nodes) - 1):
        all_nodes[i].next = all_nodes[i+1]


def connect_all_siblings(root: TreeNode):
    """
    Time: O(N)
    Space: O(N)
    """
    if root is None:
        return

    queue = deque()
    queue.append(root)
    all_nodes = []
    current_node, previous_node = None, None
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node
            all_nodes.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    for i in range(len(all_nodes) - 1):
        all_nodes[i].next = all_nodes[i+1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_tree()


main()
