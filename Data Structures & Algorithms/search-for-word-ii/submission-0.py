class Node:
    def __init__(self):
        self.d = dict()
        self.w = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Node()

        for i in words:
            c = t
            for j in i:
                if j not in c.d.keys():
                    c.d[j] = Node()
                c = c.d[j]
            c.w = i

        ans = []
        dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nr = len(board)
        nc = len(board[0])

        def dfs(r, c, n):
            letter = board[r][c]

            if letter not in n.d.keys():
                return

            ch = n.d[letter]

            if ch.w:
                ans.append(ch.w)
                ch.w = None
            
            board[r][c] = "#"
            
            for i,j in dt:
                if r + i in range(nr) and c + j in range(nc) and board[r+i][c+j] != "#":
                    dfs(r+i, c+j, ch)

            board[r][c] = letter

            if not ch.d:
                n.d.pop(letter)

        for i in range(nr):
            for j in range(nc):
                dfs(i, j, t)

        return ans