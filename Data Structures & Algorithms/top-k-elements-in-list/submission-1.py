class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [list() for _ in range(len(nums) + 1)]

        c = dict()

        for i in nums:
            c[i] = c.get(i, 0) + 1

        for i, j in c.items():
            freq[j].append(i)
            
        ans = []
        for i in range(len(nums), -1, -1):
            if len(ans) == k:
                return ans
            ans.extend(freq[i])