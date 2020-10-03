# Problem Statement
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values
# of each path equals ‘S’.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    all_paths = []
    find_paths_recursive(root, sum, [], all_paths)
    return all_paths


def find_paths_recursive(current_node: TreeNode, sum, current_path: list, all_paths: list):
    """
    Time: O(N log n)
    Space: O(N log n) log n leaf nodes depth, and n different routes
    """
    if current_node is None:
        return None

    # add the current node to the path
    current_path.append(current_node.val)

    # if the current node is a leaf and its value is equal to the sum, save the current path
    if current_node.val == sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, sum - current_node.val, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, sum - current_node.val, current_path, all_paths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack
    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print(f"Tree paths with sum {sum}: {str(find_paths(root, 23))}")


main()
