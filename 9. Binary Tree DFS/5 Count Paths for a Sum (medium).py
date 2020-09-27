# Problem Statement
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each
# path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from
# parent to child (top to bottom).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root: TreeNode, total_sum):
    return count_paths_recursive(root, total_sum, [])


def count_paths_recursive(current_node: TreeNode, total_sum, current_path):
    """
    Time: O(N2)
    Space: O(N)
    """
    if current_node is None:
        return False

    current_path.append(current_node.val)
    path_count = path_sum = 0

    # find the sum of all sub-paths in the current list
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        # if the sub-path equals to 'total_sum', we increment our path count
        if path_sum == total_sum:
            path_count += 1

    path_count += count_paths_recursive(current_node.left, total_sum, current_path)
    path_count += count_paths_recursive(current_node.right, total_sum, current_path)
    del current_path[-1]
    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.left.left = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(f"Tree has paths: {str(count_paths(root, 11))}")


main()
