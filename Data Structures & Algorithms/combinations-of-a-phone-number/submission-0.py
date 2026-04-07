class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        ans = []
        self.cur = ""

        def dfs(i):
            if i == len(digits):
                ans.append(self.cur[:])
                return

            for j in d[digits[i]]:
                self.cur += j
                dfs(i + 1)
                self.cur = self.cur[:-1]

        dfs(0)
        return ans