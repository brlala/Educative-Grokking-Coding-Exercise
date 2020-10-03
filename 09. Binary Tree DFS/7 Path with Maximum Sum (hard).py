# Problem Statement
# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. A path
# can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        self.global_max_sum = float("-inf")
        self.find_maximum_path_sum_recursive(root)
        return self.global_max_sum

    def find_maximum_path_sum_recursive(self, current_node):
        """
        Time: O(n)
        Space: O(n)
        """
        if current_node is None:
            return 0
        max_path_sum_from_left = self.find_maximum_path_sum_recursive(current_node.left)
        max_path_sum_from_right = self.find_maximum_path_sum_recursive(current_node.right)

        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)
        local_maximum_sum = max_path_sum_from_left + max_path_sum_from_right + current_node.val

        self.global_max_sum = max(local_maximum_sum, self.global_max_sum)
        return max(max_path_sum_from_left, max_path_sum_from_right) + current_node.val


def main():
    maximum_path_sum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))
    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))


main()
