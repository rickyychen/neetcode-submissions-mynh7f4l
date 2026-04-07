class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        mm = 2147483647 
        r = len(grid)
        c = len(grid[0])
        visited = set()
        tcs = list()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    tcs.append((i,j))

        children = []
        d = 1

        while tcs:
            i, j = tcs.pop()
            for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= i + x < r and 0 <= j + y < c and (i + x, j + y) not in visited and grid[i + x][j + y] == mm:
                    visited.add((i + x, j + y))
                    grid[i + x][j + y] = d
                    children.append((i + x, j + y))

            if not tcs:
                tcs = children
                d += 1
                children = []