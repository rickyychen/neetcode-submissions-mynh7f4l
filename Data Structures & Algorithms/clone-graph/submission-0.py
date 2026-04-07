"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d = {}
        cur = [node]

        while cur:
            n = cur.pop()
            if n not in d:
                d[n] = Node(n.val)
            for i in n.neighbors:
                if i not in d:
                    d[i] = Node(i.val)
                    cur.append(i)
                d[n].neighbors.append(d[i])

        return d[node]