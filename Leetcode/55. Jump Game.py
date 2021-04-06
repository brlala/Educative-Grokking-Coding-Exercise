class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Greedy
        :param nums:
        :return:
        """
        max_index = 0
        for idx, n in enumerate(nums):
            if idx > max_index:
                return False
            max_index = max(max_index, idx + nums[idx])
        return True

    def canJump(self, nums: list[int]) -> bool:
        """
        Back tracking
        :param nums:
        :return:
        """
        start, destination = 0, len(nums) - 1
        frontier_backtrack_index = destination

        # backtracking from destination
        for idx in range(len(nums)-2, -1, -1):

            # update frontier_backtrack_indx
            if idx + nums[idx] >= frontier_backtrack_index:
                frontier_backtrack_index = idx

        return frontier_backtrack_index == start

a = Solution()
a.canJump([6,2,1,0,4])