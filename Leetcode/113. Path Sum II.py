# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, res, [], targetSum)
        return res

    def dfs(self, node, res, path, target):
        if not node:
            return
        if not node.left and not node.right and target == node.val:
            res.append(path + [node.val])
            return
        self.dfs(node.left, res, path + [node.val], target - node.val)
        self.dfs(node.right, res, path + [node.val], target - node.val)
