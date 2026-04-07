class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = list()

        for i in tokens:
            if i not in "+-/*":
                s.append(int(i))
            else:
                s1, s2 = s[-2], s[-1]
                s = s[:-2]
                if i == "+":
                    s += [s1 + s2]
                elif i == "-":
                    s += [s1 - s2]
                elif i == "*":
                    s += [s1 * s2]
                elif i == "/":
                    s += [int(s1 / s2)]
                    
        return s[0]