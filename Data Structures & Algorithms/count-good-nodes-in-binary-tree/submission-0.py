# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        d = deque([root])
        mv = deque([-200])
        children = []
        childrenMv = []

        while d:
            node = d.popleft()
            v = mv.popleft()

            if node.val >= v:
                ans += 1

            if node.left:
                children.append(node.left)
                childrenMv.append(max(node.val, v))
            if node.right:
                children.append(node.right)
                childrenMv.append(max(node.val, v))

            if not d:
                print(children)
                print(childrenMv)
                d = deque(children)
                children = []
                mv = deque(childrenMv)
                childrenMv = []

        return ans