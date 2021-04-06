# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        start = head = TreeNode(None)
        node_list = []  # use for traversal later

        def preorder(root, node_list):
            if not root:
                return
            node_list.append(root)
            preorder(root.left, node_list)
            preorder(root.right, node_list)

        preorder(root, node_list)
        for n in node_list:
            head.right = n
            n.left = None
            n.right = None
            head = head.right

        return start.right
