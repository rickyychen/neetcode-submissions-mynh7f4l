class Node:
    def __init__(self, k, val, nodep = None, noden = None):
        self.k = k
        self.v = val
        self.p = nodep
        self.n = noden

class LRUCache:

    def __init__(self, capacity: int):
        self.r = Node(-1, -1)
        self.l = Node(-1, -1)
        self.l.n = self.r
        self.r.p = self.l
        self.d = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            node.p.n = node.n
            node.n.p = node.p
            left, right = self.l, self.l.n
            left.n = node
            right.p = node
            node.p = left
            node.n = right
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        node = None

        if key in self.d:
            node = self.d[key]
            node.v = value
            left, right = node.p, node.n
            left.n = right
            right.p = left
            left, right = self.l, self.l.n
            left.n = node
            right.p = node
            node.n = right
            node.p = left
        else:
            if len(self.d) == self.capacity:
                node = self.r.p
                left, right = node.p, node.n
                left.n = right
                right.p = left
                del self.d[node.k]
            node = Node(key, value, None, None)
            left, right = self.l, self.l.n
            left.n = node
            right.p = node
            node.n = right
            node.p = left
            self.d[key] = node