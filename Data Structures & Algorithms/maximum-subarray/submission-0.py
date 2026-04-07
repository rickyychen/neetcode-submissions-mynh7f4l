class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[::]

        for i in range(len(nums)):
            if i > 0:
                dp[i] = max(dp[i], dp[i] + dp[i - 1])

        return max(dp)