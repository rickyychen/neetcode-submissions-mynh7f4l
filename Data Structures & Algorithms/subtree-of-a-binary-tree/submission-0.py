# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def st(s1, s2):
            if s1 and s2:
                return s1.val == s2.val and st(s1.left, s2.left) and st(s1.right, s2.right)
            elif not (s1 or s2):
                return True
            else:
                return False

        if not subRoot:
            return True
        if not root:
            return False
        if st(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        