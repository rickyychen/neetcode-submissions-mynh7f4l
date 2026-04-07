class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(arr, lb):
            l, r = 0, len(arr) - 1
            i = -1
            while l <= r:
                m = l + (r - l) // 2
                if target == arr[m]:
                    i = m
                    if lb:
                        r = m - 1
                    else:
                        l = m + 1
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return i

        return [bs(nums, True), bs(nums, False)]