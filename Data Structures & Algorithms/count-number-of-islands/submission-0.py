class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and (i, j) not in visited and grid[i][j] == "1":
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
                return True
            return False

        for i in range(r):
            for j in range(c):
                if dfs(i, j):
                    count += 1
        return count