class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in s:
                start = i
                end = i
                while end in s:
                    end += 1
                res = max(res, end - start)
        return res