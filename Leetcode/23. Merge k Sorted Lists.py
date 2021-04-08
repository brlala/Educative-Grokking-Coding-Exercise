# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
        can also refer to grokking 15, Merge K sorted list
        Complexity
        """
        dummy = head = ListNode(None)
        count = 0
        min_heap = []
        for root in lists:
            if root:
                count += 1
                heapq.heappush(min_heap, (root.val, count, root))

        while min_heap:
            num, count, nodes = heapq.heappop(min_heap)
            head.next = nodes
            head = head.next
            if nodes.next:
                heapq.heappush(min_heap, (nodes.next.val, count, nodes.next))
        return dummy.next
