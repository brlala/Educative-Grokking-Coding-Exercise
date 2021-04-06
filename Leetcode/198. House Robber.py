class Solution:
    def rob(self, nums: list[int]) -> int:
        return self.helper(nums, len(nums) - 1)

    def helper(self, nums, index):
        if index < 0:
            return 0
        two_house_away = self.helper(nums, index - 2) + nums[index]
        one_house_away = self.helper(nums, index - 1)
        return max(two_house_away, one_house_away)

    def rob(self, nums: list[int]) -> int:
        """
        Dynamic programming
        :param nums:
        :return:
        """
        if not nums: return
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i - 1] + val, memo[i])
        return


a = Solution()
a.rob([1, 2, 3, 1])
