# Problem Statement
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root: TreeNode):
    """
    Time: O(N)
    Space: O(N)
    """
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level_values = deque()
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the value to the current values
            if left_to_right:
                current_level_values.append(current_node.val)
            else:
                current_level_values.appendleft(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            # insert the children of current node in the queue
            if current_node.right:
                queue.append(current_node.right)
        result.append(list(current_level_values))
        # reverse the direction
        left_to_right = not left_to_right
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
