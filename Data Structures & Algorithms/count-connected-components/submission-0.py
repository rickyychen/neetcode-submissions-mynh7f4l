class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i: [] for i in range(n)}

        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        visited = set()
        count = 0

        def dfs(cur, par):
            if cur in visited:
                return
            visited.add(cur)
            for e in d[cur]:
                if e == par:
                    continue
                else:
                    dfs(e, cur)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, -1)

        return count