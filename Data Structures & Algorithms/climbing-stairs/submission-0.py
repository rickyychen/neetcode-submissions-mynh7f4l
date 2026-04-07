class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        pp = 1
        p = 2

        for i in range(3, n + 1):
            cur = pp + p
            pp = p
            p = cur

        return p