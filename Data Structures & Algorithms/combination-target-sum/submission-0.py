class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(pointer, acc):
            if sum(acc) == target:
                ans.append(acc[:])
                return

            if pointer == len(nums) or sum(acc) > target:
                return

            acc.append(nums[pointer])
            dfs(pointer, acc)

            acc.pop()
            dfs(pointer + 1, acc)

        dfs(0, [])
        return ans