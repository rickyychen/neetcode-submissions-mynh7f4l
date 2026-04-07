class Solution:
    def rob(self, nums: List[int]) -> int:
        pp = 0
        p = 0

        for i in nums:
            cur = max(pp + i, p)
            pp = p 
            p = cur    
        
        return p