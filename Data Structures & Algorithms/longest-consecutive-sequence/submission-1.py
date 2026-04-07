class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        left, right = 0, 1
        ans = 1

        print(nums)

        while right < len(nums):
            if nums[right] - nums[right - 1] == 1:
                right += 1
            elif nums[right] - nums[right - 1] > 1:
                ans = max(ans, nums[right - 1] - nums[left] + 1)
                left = right
                right += 1
            else:
                right += 1

        return max(ans, nums[-1] - nums[left] + 1)