import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = []

        for i in stones:
            heapq.heappush(nums, -i)

        while len(nums) >= 2:
            s1, s2 = -heapq.heappop(nums), -heapq.heappop(nums)
            differ = abs(s1 - s2)
            if differ:
                heapq.heappush(nums, -differ)
            
        return -nums[0] if nums else 0