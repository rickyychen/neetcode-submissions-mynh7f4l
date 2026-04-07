class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = dict()
        ans = 0
        mf = 0

        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            mf = max(mf, d[s[i]])

            while (i - l + 1) - mf > k:
                d[s[l]] -= 1
                l += 1

            ans = max(ans, i - l + 1)

        return ans    