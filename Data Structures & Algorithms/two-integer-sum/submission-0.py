class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = dict()

        for i, j in enumerate(nums):
            if j in difference.keys():
                return [difference[j], i]
            difference[target - j] = i