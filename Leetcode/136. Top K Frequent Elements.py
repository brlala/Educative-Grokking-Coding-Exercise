import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq
        num_count = collections.defaultdict(int)
        for n in nums:
            num_count[n] += 1
        max_heap = [(-val, key) for key, val in num_count.items()]
        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
