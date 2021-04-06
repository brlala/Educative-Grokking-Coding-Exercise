import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for n in nums[k:]:
            heapq.heappush(pq, n)
            print(heapq.heappop(pq))
        return heapq.heappop(pq)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
