# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = collections.deque([root])
        res = []
        order_flag = False
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                if order_flag:
                    current = queue.pop()
                    level.append(current.val)
                    if current.right:
                        # change append order so you don't affect the current queue
                        queue.appendleft(current.right)
                    if current.left:
                        queue.appendleft(current.left)
                else:
                    current = queue.popleft()
                    level.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)

            order_flag = not order_flag
            res.append(level)
        return res
