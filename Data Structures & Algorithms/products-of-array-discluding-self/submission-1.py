class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1 for _ in range(len(nums))]
        back = [1 for _ in range(len(nums))]

        #front first 
        for i, j in enumerate(nums):
            if i == len(nums) - 1:
                continue
            front[i + 1] = front[i] * j
        
        #back
        for i, j in enumerate(nums[::-1]):
            if i == len(nums) - 1:
                continue
            back[len(nums) - i - 1 - 1] = back[len(nums) - i - 1] * j

        return [i * j for i, j in zip(front, back)]