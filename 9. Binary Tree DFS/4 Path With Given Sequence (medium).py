# Problem Statement
# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root: TreeNode, sequence):
    if not root:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node: TreeNode, sequence, sequence_index):
    """
    Time: O(N)
    Space: O(N)
    """
    if current_node is None:
        return False

    sequence_length = len(sequence)

    # no use checking anymore if sequence length is lower, early termination
    if sequence_index >= sequence_length or current_node.val != sequence[sequence_index]:
        return False

    # stop condition
    if current_node.left is None and current_node.right is None and sequence_index == sequence_length -1:
        return True

    left_exist = find_path_recursive(current_node.left, sequence, sequence_index + 1)
    right_exist = find_path_recursive(current_node.right, sequence, sequence_index + 1)
    return left_exist or right_exist


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(f"Tree has path sequence: {str(find_path(root, [1, 1, 7]))}")
    print(f"Tree has path sequence: {str(find_path(root, [1, 1, 6]))}")


main()
