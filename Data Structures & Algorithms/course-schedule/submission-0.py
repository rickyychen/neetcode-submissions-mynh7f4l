class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        for i, j in prerequisites:
            inDegree[j] += 1
            d[i].append(j)

        s = []
        for i, j in enumerate(inDegree):
            if j == 0:
                s.append(i)

        finish = 0
        while s:
            n = s.pop()
            finish += 1
            
            for nei in d[n]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    s.append(nei)

        return finish == numCourses