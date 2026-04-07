class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 10 ** 10

        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            t = 0
            for i in piles:
                t += i // mid
                if i % mid:
                    t += 1
            if t <= h:
                right = mid - 1
                ans = min(ans, mid)
            else:
                left = mid + 1

        return ans