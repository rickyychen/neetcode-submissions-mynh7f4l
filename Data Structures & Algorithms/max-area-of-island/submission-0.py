class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        r = len(grid)
        c = len(grid[0])
        visited = set()

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and (i, j) not in visited and grid[i][j]:
                visited.add((i, j))
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0

        for i in range(r):
            for j in range(c):
                ans = max(ans, dfs(i, j))

        return ans