class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = dict()
        a = 0
        c = 0

        for i in range(len(s)):
            if s[i] in d.keys():
                a = max(i - c, a)
                c = max(c, d[s[i]] + 1)
                d[s[i]] = i
            else:
                d[s[i]] = i
                a = max(i - c + 1, a)

        return a