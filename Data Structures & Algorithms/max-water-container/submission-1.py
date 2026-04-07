class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        ans = 0

        while left < right and right < len(heights):
            ans = max(ans, min(heights[left], heights[right]) * (right - left))

            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1

        return ans