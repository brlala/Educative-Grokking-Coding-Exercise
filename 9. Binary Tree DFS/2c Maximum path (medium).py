# Problem Statement
# Given a binary tree, find the root-to-leaf path with the maximum sum.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_paths(root: TreeNode) -> int:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    :param root:
    :return:
    """
    max_path = float("-inf")  # placeholder to be updated

    def get_max_gain(current_node):
        nonlocal max_path  # This tells that max_path is not a local variable
        if current_node is None:
            return 0

        gain_on_left = max(get_max_gain(current_node.left), 0)  # Read the part important observations
        gain_on_right = max(get_max_gain(current_node.right), 0)  # Read the part important observations

        current_max_path = current_node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
        max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

        return current_node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

    get_max_gain(root)  # Starts the recursion chain
    return max_path


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.left.left = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"All tree paths : {str(find_max_paths(root))}")


main()
