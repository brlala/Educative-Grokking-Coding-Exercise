"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        O(2n)
        """
        dic = dict()
        m = n = head
        # Create old node to new node
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        dict with old Nodes as keys and new Nodes as values. Doing so allows us to create node's
        next and random as we iterate through the list from head to tail. Otherwise, we need to go
        through the list backwards. defaultdict() is an efficient way of handling missing keys
        """
        map_new = collections.defaultdict(lambda: Node(0, None, None))
        map_new[
            None] = None  # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop

        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]