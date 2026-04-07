class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        p = set()
        a = set()

        def dfs(i, j, visited, h):
            if (i, j) in visited or i < 0 or i == r or j < 0 or j == c or heights[i][j] < h:
                return
            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for i in range(r):
            dfs(i, 0, p, heights[i][0])
            dfs(i, c - 1, a, heights[i][c - 1])

        for j in range(c):
            dfs(0, j, p, heights[0][j])
            dfs(r - 1, j, a, heights[r - 1][j])

        ans = []

        for i in range(r):
            for j in range(c):
                if (i, j) in p and (i, j) in a:
                    ans.append([i, j])     

        return ans