class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = []
        fresh = set()
        r = len(grid)
        c = len(grid[0])
        visited = set()
        children = []
        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rot.append((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))

        while rot:
            i, j = rot.pop()

            for x, y in ((0, 1), (1,0), (-1, 0), (0, -1)):
                if 0 <= x + i < r and 0 <= j + y < c and (x + i, j + y) not in visited and (x + i, j + y) in fresh:
                    visited.add((i + x, j + y))
                    fresh.remove((i + x, j + y))
                    children.append((i + x, j + y))
            
            if not rot:
                if children:
                    count += 1
                rot = children
                children = []

        return -1 if fresh else count