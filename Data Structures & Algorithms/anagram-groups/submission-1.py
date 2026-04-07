class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j) - ord('a')] += 1
            v = d.get(tuple(freq), [])
            v.append(i)
            d[tuple(freq)] = v

        return list(d.values())