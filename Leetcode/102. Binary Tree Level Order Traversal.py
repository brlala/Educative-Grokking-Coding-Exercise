# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while root and queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level_values.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(current_level_values)
        return res
