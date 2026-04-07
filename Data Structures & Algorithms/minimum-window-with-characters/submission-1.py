class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dt = dict()
        ds = dict()

        for i in t:
            dt[i] = dt.get(i, 0) + 1

        req = len(dt)
        have = 0
        res = [-100, 100]
        rl = 1000000
        l = 0

        for i in range(len(s)):
            c = s[i]
            ds[c] = ds.get(c, 0) + 1

            if c in dt and ds[c] == dt[c]:
                have += 1

            while have == req:
                if (i - l + 1) < rl:
                    res = [l, i]
                    rl = i - l + 1

                ds[s[l]] -= 1
                if s[l] in dt and ds[s[l]] < dt[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if rl != 1000000 else ""