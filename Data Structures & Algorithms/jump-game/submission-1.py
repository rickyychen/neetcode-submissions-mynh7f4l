class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        q = [(0, nums[0])] #index, ability
        visited = set([0])
        children = []


        while q:
            ind, ab = q.pop()
            for i in range(ab + 1):
                if ind + i not in visited:
                    if ind + i >= len(nums) - 1:
                        return True
                    else:
                        visited.add(ind + i)
                        children.append((ind + i, nums[ind + i]))
            if not q:
                q = children
                children = []

        return False