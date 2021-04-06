class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirstIndex(0, len(nums) - 1, nums, target)
        second = self.findLastIndex(0, len(nums) - 1, nums, target)
        return [first, second]

    def findFirstIndex(self, low, high, nums, target):
        res = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                res = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res

    def findLastIndex(self, low, high, nums, target):
        res = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                res = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res
