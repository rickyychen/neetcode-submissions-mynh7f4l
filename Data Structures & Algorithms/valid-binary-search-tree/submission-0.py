# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        d = deque([root])
        children = []
        mv = deque([(-10000, 10000)])
        childrenMv = []

        while d:
            node = d.popleft()
            mn, mx = mv.popleft()

            if node.val > mn and node.val < mx:
                if node.left:
                    children.append(node.left)
                    childrenMv.append((mn, min(node.val, mx)))
                if node.right:
                    children.append(node.right)
                    childrenMv.append((max(mn, node.val), mx))

                if not d:
                    d = deque(children)
                    children = []
                    mv = deque(childrenMv)
                    childrenMv = []
            else:
                return False

        return True