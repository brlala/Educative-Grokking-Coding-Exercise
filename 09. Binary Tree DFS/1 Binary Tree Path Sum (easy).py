# Problem Statement
# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the
# node values of that path equals ‘S’.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    """
    Time: O(N)
    Space: O(N) worst case if tree is a linked list
    """
    if root is None:
        return False

    # if the current node is leaf and equals to sum
    if root.left is None and root.right is None and root.val == sum:
        return True

    # recursively call to traverse left and right sub-tree
    # returns true if any of the two recursive calls becomes true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
