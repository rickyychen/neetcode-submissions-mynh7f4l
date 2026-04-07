# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this should be a queue
        if not root:
            return []
        
        ans = []        
        d = deque([root])
        children = []
        level = []

        while d:
            node = d.popleft()
            level.append(node.val)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            if not d:
                d = deque(children)
                ans.append(level)
                children = []
                level = []

        return ans