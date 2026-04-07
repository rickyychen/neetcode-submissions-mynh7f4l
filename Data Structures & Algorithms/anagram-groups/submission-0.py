class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rep = 26
        d = dict()

        for i in strs:
            r = [0] * rep
            for j in i:
                r[ord(j) - ord('a')] += 1
            r = tuple(r)
            d.setdefault(r, []).append(i)

        return list(d.values())