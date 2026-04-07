import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []

        for i, j in points:
            heapq.heappush(nums, (i**2 + j ** 2, (i, j)))

        return [heapq.heappop(nums)[-1] for i in range(k)]