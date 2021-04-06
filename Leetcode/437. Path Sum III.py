# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, target):
        """
        This uses O(n^2) brute force method
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return
            # dfs break down
        self.test(node, target)  # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1

        # test break down
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)

    def pathSum(self, root, target):
        """
        This is O(n) linear method
        """
        self.numOfPaths = 0
        cache = {0: 1}
        self.memoization(root, target, 0, cache)
        return self.numOfPaths

    def memoization(self, node, target, currPathSum, cache):
        # exit conidtion:
        if not node:
            return
        currPathSum += node.val
        oldPathSum = currPathSum - target
        if oldPathSum in cache:
            self.numOfPaths += cache[oldPathSum]

        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        self.memoization(node.left, target, currPathSum, cache)
        self.memoization(node.right, target, currPathSum, cache)
        cache[currPathSum] -= 1
