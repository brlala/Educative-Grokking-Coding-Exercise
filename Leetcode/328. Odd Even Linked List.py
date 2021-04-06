# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead = start1 = ListNode(0)
        evenHead = start2 = ListNode(0)
        current = 0

        while head:
            if current % 2:
                evenHead.next, evenHead = head, head
            else:
                oddHead.next, oddHead = head, head
            head = head.next
            current += 1
        oddHead.next, evenHead.next = start2.next, None
        return start1.next

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head  # Both of them point at the first node of the target linked list
        even = head.next  # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = eHead
        return head