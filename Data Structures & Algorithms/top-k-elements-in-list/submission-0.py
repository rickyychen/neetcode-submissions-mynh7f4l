class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            d[i] = d.get(i, 0) + 1

        for i, j in d.items():
            freq[j].append(i)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            res.extend(freq[i])
            if len(res) == k:
                return res

        return res