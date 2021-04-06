# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return
        carry = 0
        dummy_head = ans = ListNode()
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = carry // 10, carry % 10
            # carry, val = divmod(carry, 10)
            node = ListNode(val)
            ans.next = node
            ans = ans.next
        return dummy_head.next
