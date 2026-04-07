# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -100000

        def dfs(node):
            if not node:
                return 0

            leftSide = max(dfs(node.left), 0)
            rightSide = max(dfs(node.right), 0)

            cur = node.val + leftSide + rightSide
            self.ans = max(self.ans, cur)

            return node.val + max(leftSide, rightSide)

        dfs(root)
        return self.ans