class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for i in range(len(height))]
        postfix = [0 for i in range(len(height))]

        for i, j in enumerate(height):
            if i > 0:
                prefix[i] = max(j, prefix[i - 1])
                postfix[len(height) - i - 1] = max(height[len(height) - i - 1], postfix[len(height) - i])
            else:
                prefix[i] = j
                postfix[len(height) - i - 1] = height[len(height) - i - 1]

        ans = 0
        for i in range(len(height)):
            ans += min(prefix[i], postfix[i]) - height[i]

        return ans