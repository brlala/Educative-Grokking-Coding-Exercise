# Problem Statement
# Given a binary tree, return all root-to-leaf paths.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_all_paths(root):
    all_paths = []
    find_paths_recursive(root, [], all_paths)
    return all_paths


def find_paths_recursive(current_node: TreeNode, current_path: list, all_paths: list):
    """
    Time: O(N log n)
    Space: O(N log n) log n leaf nodes depth, and n different routes
    """
    if current_node is None:
        return None

    # add the current node to the path
    current_path.append(current_node.val)

    # if the current node is a leaf and its value is equal to the sum, save the current path
    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, current_path, all_paths)

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
    root.right.right.right = TreeNode(22)
    root.right.right.right.left = TreeNode(33)
    root.right.right.right.right = TreeNode(44)
    print(f"All tree paths : {str(find_all_paths(root))}")


main()
