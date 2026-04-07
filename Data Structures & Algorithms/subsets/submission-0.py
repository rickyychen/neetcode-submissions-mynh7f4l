class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(pointer, acc):
            if pointer == len(nums):
                ans.append(acc[:])
                return

            acc.append(nums[pointer])
            dfs(pointer + 1, acc)

            acc.pop()
            dfs(pointer + 1, acc)

        dfs(0, [])
        return ans