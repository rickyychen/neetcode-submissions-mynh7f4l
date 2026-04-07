class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i: [] for i in range(numCourses)}
        ind = [0] * numCourses

        for i, j in prerequisites:
            d[i].append(j)
            ind[j] += 1

        s = []
        for i, j in enumerate(ind):
            if j == 0:
                s.append(i)

        finish = 0
        ans = []
        while s:
            n = s.pop()
            finish += 1
            ans.append(n)
            for nei in d[n]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    s.append(nei)

        return ans[::-1] if finish == numCourses else []