class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d1 = [0 for _ in range(26)]
        d2 = [0 for _ in range(26)]

        for i, j in zip(s1, s2):
            d1[ord(i) - ord('a')] += 1
            d2[ord(j) - ord('a')] += 1

        if d1 == d2:
            return True

        for i in range(len(s1), len(s2)):
            d2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            d2[ord(s2[i]) - ord('a')] += 1
            if d1 == d2:
                return True

        return False