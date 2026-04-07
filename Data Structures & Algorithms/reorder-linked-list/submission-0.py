# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return
        
        
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next

        p, c = None, s
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n

        f, s = head, p
        while s.next:
            fn, sn = f.next, s.next
            f.next = s
            s.next = fn
            f = fn
            s = sn