class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        https://leetcode.com/problems/last-stone-weight-ii/discuss/294888/JavaC%2B%2BPython-Easy-Knapsacks-DP
        Time O(NS),
        Space O(S) space, where S = sum(A).
        """
        dp = {0}
        sum_all_stones = sum(stones)
        for s in stones:
            dp |= {s + i for i in dp}
        return min(abs(sum_all_stones - i - i) for i in dp)  # s1 + s2 = SUM, S1-S2 = (SUM - S2) - S2

    def lastStoneWeightII(self, A):
        dp = {0}
        for a in A:
            dp = {a + x for x in dp} | {abs(a - x) for x in dp}
        return min(dp)


a = Solution()
a.lastStoneWeightII([31, 26, 33, 21, 40])
