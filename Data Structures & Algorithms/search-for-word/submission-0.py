class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()


        def dfs(i, j, ind):
            if ind == len(word):
                return True
            
            res = False
            if 0 <= i < len(board[0]) and 0 <= j < len(board) and (i, j) not in visited and board[j][i] == word[ind]:
                visited.add((i, j))
                res = dfs(i + 1, j, ind + 1) or dfs(i, j + 1, ind + 1) or dfs(i - 1, j, ind + 1) or dfs(i, j - 1, ind + 1)
                visited.remove((i, j))

            return res

        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x, y, 0):
                    return True

        return False