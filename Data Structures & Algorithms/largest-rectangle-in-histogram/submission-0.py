class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = -1

        for i, j in enumerate(heights):
            while s and j < heights[s[-1]]:
                cur = s.pop()
                left = s[-1] if s else -1
                m = max(m, heights[cur] * (i - left - 1))
            s.append(i)

        while s:
            cur = s.pop()
            left = s[-1] if s else -1
            m = max(m, heights[cur] * (len(heights) - left - 1))

        return m