# Problem Statement
# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a
# number. Find the total sum of all the numbers represented by all paths.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root: TreeNode):
    return find_sum_of_path_numbers_recursive(root, 0)


def find_sum_of_path_numbers_recursive(current_node: TreeNode, path_sum):
    """
    Time: O(N)
    Space: O(N)
    """
    if current_node is None:
        return 0

    path_sum = path_sum * 10 + current_node.val

    # stop condition
    if current_node.left is None and current_node.right is None:
        return path_sum

    left_sum = find_sum_of_path_numbers_recursive(current_node.left, path_sum)
    right_sum = find_sum_of_path_numbers_recursive(current_node.right, path_sum)
    return left_sum + right_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(f"Total Sum of path numbers: {str(find_sum_of_path_numbers(root))}")


main()
