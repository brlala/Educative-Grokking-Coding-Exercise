# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-right-side-view/discuss/56248/Python-easy-to-understand-BFS-solution-(level-by-level)
        :param root:
        :return:
        """
        if not root:
            return
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            val = 0
            for _ in range(size):
                current_node = queue.popleft()
                val = current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(val)
        return res
