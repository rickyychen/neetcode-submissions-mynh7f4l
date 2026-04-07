class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        r = len(board)
        c = len(board[0])
        circles = set()

        for i in range(r):
            if board[i][0] == "O":
                circles.add((i, 0))
            if board[i][c - 1] == "O":
                circles.add((i, c - 1))

        for j in range(c):
            if board[0][j] == "O":
                circles.add((0, j))
            if board[r - 1][j] == "O":
                circles.add((r - 1, j))

        def dfs(i, j):
            if (i, j) in visited or i < 0 or i == r or j < 0 or j == c or board[i][j] == "X":
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i, j in circles:
            dfs(i, j)

        for i in range(r):
            for j in range(c):
                if (i, j) not in visited:
                    board[i][j] = "X"