class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(pointer, differ):
            if differ == 0:
                ans.append(path[:])
                return

            for i in range(pointer, len(candidates)):
                if i > pointer and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > differ:
                    break

                path.append(candidates[i])
                dfs(i + 1, differ - candidates[i])
                path.pop()


        dfs(0, target)
        return ans