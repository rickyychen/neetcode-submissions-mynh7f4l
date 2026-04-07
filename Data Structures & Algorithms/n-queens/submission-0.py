class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        ans = []

        def dfs(nq):
            if nq == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for i in range(n):
                if self.isSafe(nq, i, board):
                    board[nq][i] = "Q"
                    dfs(nq + 1)
                    board[nq][i] = "."

        dfs(0)
        return ans

    def isSafe(self, r, c, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True