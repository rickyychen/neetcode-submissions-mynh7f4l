# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        acc = ListNode()

        for i in lists:
            acc.next = self.merge(acc.next, i)

        return acc.next

    def merge(self, l1, l2):
        a = ListNode()
        c = a

        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next

        while l1:
            c.next = l1
            c, l1 = c.next, l1.next

        while l2:
            c.next = l2
            c, l2 = c.next, l2.next

        return a.next