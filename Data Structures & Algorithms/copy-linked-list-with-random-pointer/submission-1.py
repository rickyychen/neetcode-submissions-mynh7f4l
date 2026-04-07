"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = head
        d = dict()

        while c:
            d[c] = Node(c.val) 
            c = c.next

        c = head
        while c:
            d[c].next = d[c.next] if c.next in d else None
            d[c].random = d[c.random] if c.random in d else None
            c = c.next

        return d[head] if head else None        