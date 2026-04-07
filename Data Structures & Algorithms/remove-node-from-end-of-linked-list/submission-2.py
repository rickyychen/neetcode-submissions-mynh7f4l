# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = head
        l = 0

        while c:
            l += 1
            c = c.next

        if l == n:
            return head.next

        i = 0
        c = head

        for i in range(l - n - 1):
            c = c.next

        c.next = c.next.next

        return head