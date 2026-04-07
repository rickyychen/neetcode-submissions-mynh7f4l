from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        mh = [-i for i in counter.values()]
        heapq.heapify(mh)

        time = 0
        q = deque()

        while mh or q:
            if not mh:
                time = q[0][1]
            else:
                time += 1
                ocur = heapq.heappop(mh) + 1
                if ocur:
                    q.append((ocur, time + n))
            if q and q[0][1] <= time:
                heapq.heappush(mh, q.popleft()[0])

        return time