import bisect
import heapq


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
        dynamic programming
        Time O(NlogN) for sorting
        Time O(NlogN) for binary search for each job
        Space O(N)
        """
        # we will decide between doing the job or not doing the job, sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]  # end time, profit, we make profit = 0 when t = 0
        for start, end, profit in jobs:
            i = bisect.bisect(dp, [start + 1]) - 1  # find largest profit we can make before start time
            if dp[i][1] + profit > dp[-1][1]:  # if profit is more, do it
                dp.append([end, dp[i][1] + profit])
        return dp[-1][1]  # get the profit when time ends

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409358/Python
        using minHeap
        """
        # sort by start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        total = 0
        minHeap = []

        # use (end, totalprofit) minHeap to maintain all job schedules, only compatible schedules will be kept
        for start, end, current_profit in jobs:
            while minHeap and minHeap[0][0] <= start:  # minimum end time less than start, get max profit up to this point
                _, profit = heapq.heappop(minHeap)
                total = max(total, profit)
            heapq.heappush(minHeap, (end, total + current_profit))

        # iterate through all schedules to find max profit
        while minHeap:
            _, profit = heapq.heappop(minHeap)
            total = max(total, profit)
        return total


a = Solution()
print(a.jobScheduling(startTime=[1, 2, 2, 3, 3], endTime=[3, 4, 4, 5, 6], profit=[50, 10, 140, 40, 70]))
