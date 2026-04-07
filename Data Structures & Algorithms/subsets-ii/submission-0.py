class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []

        def dfs(ind):
            if ind == len(nums):
                ans.append(cur[:])
                return

            cur.append(nums[ind])
            dfs(ind + 1)
            cur.pop()

            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1
            dfs(ind + 1)

        dfs(0)
        return ans