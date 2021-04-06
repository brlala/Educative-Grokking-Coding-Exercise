# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        naive programming
        """
        if not root:
            return 0

        value = 0
        if root.left:
            value += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            value += self.rob(root.right.left) + self.rob(root.right.right)

        return max(value + root.val, self.rob(root.left) + self.rob(root.right))

    def rob(self, root: TreeNode) -> int:
        """
        memoization
        """

        def helper(root, memo):
            if root in memo:
                return memo[root]

            if not root:
                return 0
            value = 0
            if root.left:
                value += helper(root.left.left, memo) + helper(root.left.right, memo)

            if root.right:
                value += helper(root.right.left, memo) + helper(root.right.right, memo)

            max_value = max(value + root.val, helper(root.left, memo) + helper(root.right, memo))
            memo[root] = max_value
            return max_value

        memo = {}
        return helper(root, memo)

    def rob(self, root: TreeNode) -> int:
        """
        dynamic programming
        """

        def helper_dp(root):
            if not root:
                return (0, 0)
            left = helper_dp(root.left)
            right = helper_dp(root.right)

            # res 0 is root not robbed, 1 is root robbed
            root_not_robbed = max(left[0], left[1]) + max(right[0], right[1])
            root_robbed = root.val + left[0] + right[0]
            res = (root_not_robbed, root_robbed)
            return res

        return max(helper_dp(root))
