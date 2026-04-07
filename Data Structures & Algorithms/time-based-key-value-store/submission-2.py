class TimeMap:

    def __init__(self):
        self.mp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        v = self.mp.get(key, list())
        v.append((value, timestamp))
        self.mp[key] = v

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mp.keys():
            l, r = 0, len(self.mp[key]) - 1
            ans = ""
            while l <= r:
                m = l + (r - l) // 2
                if self.mp[key][m][1] <= timestamp:
                    ans = self.mp[key][m][0]
                    l = m + 1
                else:
                    r = m - 1
            return ans
        return ""
