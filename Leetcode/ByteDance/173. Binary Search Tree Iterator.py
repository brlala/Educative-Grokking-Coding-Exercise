# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)
    """

    def __init__(self, root: TreeNode):
        self.root = root
        self.current_node = root
        self.stack = []

    def next(self) -> int:
        while self.current_node:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left
        next = self.stack.pop()
        self.current_node = next.right
        return next.val

    def hasNext(self) -> bool:
        return self.current_node is not None or len(self.stack)!=0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()