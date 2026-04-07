class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        d = {i: [] for i in range(n)}

        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        visited = set()

        def dfs(cur, par):
            if cur in visited:
                return False
            visited.add(cur)

            for e in d[cur]:
                if e == par:
                    continue
                else:
                    if not dfs(e, cur):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)