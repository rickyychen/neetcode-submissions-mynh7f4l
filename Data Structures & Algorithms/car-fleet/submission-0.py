class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = -1
        ans = 0
        ps = [(i, j) for i, j in zip(position, speed)]

        ps.sort(key=lambda x: (x[0], x[1]), reverse = True)

        print(ps)

        while ps:
            i, j = ps[0]
            ps = ps[1:]
            t = (target - i) / j

            if t > m:
                m = t
                ans += 1

        return ans