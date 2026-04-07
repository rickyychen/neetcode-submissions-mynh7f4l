class Node:
    def __init__(self):
        self.d = dict()
        self.w = False

class PrefixTree:

    def __init__(self):
        self.r = Node()

    def insert(self, word: str) -> None:
        c = self.r

        for i in word:
            if i in c.d.keys():
                c = c.d[i]
            else:
                c.d[i] = c.d.get(i, Node())
                c = c.d[i]
        c.w = True

    def search(self, word: str) -> bool:
        c = self.r

        for i in word:
            if i in c.d.keys():
                c = c.d[i]
            else:
                return False
        return c.w

    def startsWith(self, prefix: str) -> bool:
        c = self.r
        for i in prefix:
            if i in c.d.keys():
                c = c.d[i]
            else:
                return False
        return True