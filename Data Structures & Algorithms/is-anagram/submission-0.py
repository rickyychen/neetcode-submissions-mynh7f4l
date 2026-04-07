class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = [0] * 26
        lt = [0] * 26

        for i, j in zip(s, t):
            ls[ord(i) - ord('a')] += 1
            lt[ord(j) - ord('a')] += 1

        return ls == lt
