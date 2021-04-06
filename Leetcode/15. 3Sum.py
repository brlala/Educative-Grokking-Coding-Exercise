class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # never skip the first
                continue
            target = nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] + target == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    left = left + 1
                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1
                elif nums[left] + nums[right] + target < 0:
                    left += 1
                elif nums[left] + nums[right] + target > 0:
                    right -= 1
        return result

a= Solution()
a.threeSum([-1,0,1,2,-1,-4])
print(a.threeSum([0,0,0]))