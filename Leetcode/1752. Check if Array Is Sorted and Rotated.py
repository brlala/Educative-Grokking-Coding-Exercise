class Solution:
    def check(self, nums: List[int]) -> bool:
        count_reversal = 0
        for i in range(len(nums)):  # start from 0 because we want to compare between different list boundaries too
            if nums[i-1] > nums[i]:
                count_reversal += 1
        return count_reversal <= 1