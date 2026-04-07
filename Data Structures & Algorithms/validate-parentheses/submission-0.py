class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}

        st = []
        for i in s:
            if i not in d.keys():
                st.append(i)
            else:
                if st:
                    if d[i] == st[-1]:
                        st = st[:-1]
                    else:
                        return False
                else:
                    return False
        if st:
            return False
        else:
            return True