class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        DFS
        """
        self.num_of_ways = 0

        def helper(nums, pos, current_sum):
            if pos >= len(nums):
                if current_sum == 0:
                    self.num_of_ways += 1
                return
            helper(nums, pos + 1, current_sum + nums[pos])
            helper(nums, pos + 1, current_sum - nums[pos])

        helper(nums, 0, S)
        return self.num_of_ways

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        DFS + memoization
        """
        memo = {}

        def helper(nums, pos, current_sum):
            if (pos, current_sum) not in memo:
                if pos == len(nums):
                    if current_sum == 0:
                        ways = 1
                    else:
                        ways = 0
                else:
                    ways = helper(nums, pos + 1, current_sum + nums[pos]) + helper(nums, pos + 1, current_sum - nums[pos])
                memo[(pos, current_sum)] = ways
            return memo[(pos, current_sum)]

        helper(nums, 0, S)
        return memo[(0, S)]