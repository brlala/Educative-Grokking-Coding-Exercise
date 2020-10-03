# Problem Statement
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root: TreeNode):
    """
    Time: O(N)
    Space: O(N)
    """
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level_sum = 0.0
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the value to the current values
            current_level_sum += current_node.val
            if current_node.left:
                queue.append(current_node.left)
            # insert the children of current node in the queue
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level_sum / level_size)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(find_level_averages(root)))


main()
