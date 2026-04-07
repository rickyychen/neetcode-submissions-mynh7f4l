class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pp = 0
        p = 0

        for i in range(2, len(cost) + 1):
            cur = min(pp + cost[i - 2], p + cost[i - 1])
            pp = p
            p = cur

        return p