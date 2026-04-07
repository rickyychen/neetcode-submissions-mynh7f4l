# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = deque([root])
        ans = []
        children = []

        while d:
            right = d[-1]
            node = d.popleft()
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            if node == right:
                d = deque(children)
                ans.append(node.val)
                children = []

        return ans