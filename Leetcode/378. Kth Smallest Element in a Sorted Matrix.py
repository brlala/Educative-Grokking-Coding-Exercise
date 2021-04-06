from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time complexity: nlgn
        space complexity: n*m
        """
        combined_list = []
        for m in matrix:
            combined_list.extend(m)
        combined_list.sort()
        return combined_list[k - 1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time complexity: klgM, M is matrix
        space complexity: O(k)
        """
        min_heap = []
        for i in range(len(matrix)):
            heappush(min_heap, (matrix[i][0], 0, matrix[i]))
        number_count = number = 0
        while min_heap:
            number, i, num_list = heappop(min_heap)
            number_count += 1
            if number_count == k:
                break
            if len(num_list) > i + 1:
                heappush(min_heap, (num_list[i + 1], i + 1, num_list))

        return number