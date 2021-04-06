# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_preorder(root):
    if not root:
        return
    print(root.val, end=' ')
    print_preorder(root.left)
    print_preorder(root.right)


def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=' ')
    print_inorder(root.right)


def print_postorder(root):
    if not root:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val, end=' ')


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        pop equal amount, so don't need index in preorder
        :param preorder:
        :param inorder:
        :return:
        """
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_index])
            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index + 1:])
            return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
a = Solution()
tree = a.buildTree(preorder, inorder)
print_preorder(tree)
print()
print_inorder(tree)
print()
print_postorder(tree)
