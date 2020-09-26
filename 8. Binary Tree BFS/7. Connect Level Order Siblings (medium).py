# Problem Statement
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + ' ', end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


def connect_level_order_siblings(root: TreeNode):
    """
    This method is written by me, more like functional programming
    Time: O(N)
    Space: O(N)
    """
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        previous_node = None
        nodes_to_connect = []
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
                nodes_to_connect.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
                nodes_to_connect.append(current_node.right)
        for i in range(len(nodes_to_connect) - 1):
            nodes_to_connect[i].next = nodes_to_connect[i+1]


def connect_level_order_siblings(root: TreeNode):
    """
    Time: O(N)
    Space: O(N)
    """
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        previous_node = None
        nodes_to_connect = []
        level_size = len(queue)
        # connect all nodes of this level
        for _ in range(level_size):
            current_node = queue.popleft()
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node

            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
                nodes_to_connect.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
                nodes_to_connect.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
