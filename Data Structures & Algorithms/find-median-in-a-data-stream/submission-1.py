import heapq
class MedianFinder:

    def __init__(self):
        self.l = [] #max
        self.r = [] #min

    def addNum(self, num: int) -> None:
        heapq.heappush(self.l, -num)
        heapq.heappush(self.r, -heapq.heappop(self.l))

        if len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))

    def findMedian(self) -> float:
        if len(self.l) == len(self.r):
            return (-self.l[0] + self.r[0]) / 2
        return -self.l[0]