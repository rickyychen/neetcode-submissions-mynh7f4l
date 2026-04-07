"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st = sorted([i.start for i in intervals])
        en = sorted([i.end for i in intervals])
        n = len(intervals)

        res, count = 0, 0
        s, e = 0, 0

        while s < n:
            if st[s] < en[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)


        return res