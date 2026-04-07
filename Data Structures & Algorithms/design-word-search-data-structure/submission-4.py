class Node:
    def __init__(self):
        self.d = dict()
        self.w = False

class WordDictionary:

    def __init__(self):
        self.r = Node()

    def addWord(self, word: str) -> None:
        c = self.r

        for i in word:
            if i in c.d.keys():
                c = c.d[i]
            else:
                if i not in c.d.keys():
                    c.d[i] = Node()
                c = c.d[i]
        c.w = True

    def search(self, word: str) -> bool:
        s = [(self.r, 0)]

        while s:
            e = s.pop()
            i, j = e
            if j == len(word):
                if i.w:
                    return True
                continue
            else:
                if word[j] == ".":
                    for v in i.d.values():
                        s.append((v, j + 1))
                else:
                    if word[j] in i.d.keys():
                        s.append((i.d[word[j]], j + 1))

        return False