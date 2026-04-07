class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.cur = ""

        def dfs(op, cl):
            if op == cl == n:
                ans.append(self.cur[:])
                return

            if op < n:
                self.cur += "("
                dfs(op + 1, cl)
                self.cur = self.cur[:-1]

            if cl < op:
                self.cur += ")"
                dfs(op, cl + 1)
                self.cur = self.cur[:-1]

        dfs(0, 0)
        return ans