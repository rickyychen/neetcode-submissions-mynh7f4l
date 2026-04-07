from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = {}
        visited = set([beginWord])

        for w in wordList:
            for i in range(len(w)):
                p = w[:i] + "*" + w[i + 1:]
                if p not in d:
                    d[p] = [w]
                else:
                    d[p].append(w)

        q = deque([(beginWord, 1)])

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                p = word[:i] + "*" + word[i + 1:]
                if p in d:
                    for nei in d[p]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append([nei, step + 1])

        return 0