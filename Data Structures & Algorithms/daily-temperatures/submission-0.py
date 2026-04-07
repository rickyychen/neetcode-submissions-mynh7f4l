class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        s = []

        for i in range(len(temperatures)):
            if s:
                while s and temperatures[i] > temperatures[s[-1]]:
                    ans[s[-1]] = i - s[-1]
                    s = s[:-1]
                s.append(i)
            else:
                s.append(i)

        return ans