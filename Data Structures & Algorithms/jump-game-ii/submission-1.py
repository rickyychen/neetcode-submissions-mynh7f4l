class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        s = [(0, nums[0], 0)]
        visited = set()
        children = []

        while s:
            ind, ab, count = s.pop()
            if ind in visited:
                continue
            visited.add(ind)
            count += 1
            for i in range(1, ab + 1):
                nxt = ind + i
                if nxt >= len(nums) - 1:
                    return count
                else:
                    children.append((nxt, nums[nxt], count))

            if not s:
                s = children
                children = []