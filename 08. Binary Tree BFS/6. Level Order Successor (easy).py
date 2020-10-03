# Problem Statement
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root: TreeNode, key):
    """
    Time: O(N)
    Space: O(N)
    """
    result = None
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            if current_node.val == key:
                return queue.popleft()
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)
    result = find_successor(root, 10)
    if result:
        print(result.val)


main()
