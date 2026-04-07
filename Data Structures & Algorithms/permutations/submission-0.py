class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        used = [False] * n
        cur = [0] * n


        def dfs(ind):

            if ind == n:
                ans.append(cur[:])
                return

            for i, j in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    cur[ind] = j
                    dfs(ind + 1)
                    used[i] = False

        dfs(0)
        return ans