class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ""

        for i in s:
            if i.isalnum():
                v += i

        v = v.lower()
        print(v)

        for i in range(len(v) // 2):
            if v[i] != v[len(v) - i - 1]:
                return False
        return True