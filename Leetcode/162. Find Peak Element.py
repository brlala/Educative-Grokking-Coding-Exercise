class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 1. always increasing  -> the right-most element is the peak
        # 2. always decreasing  -> the left-most element is the peak
        # 3. first increasing then decreasing -> the pivot point is the peak
        # 4. first decreasing then increasing -> the left-most element is the peak

        left = 0
        right = len(nums) - 1

        # handle scenario #3 #4
        while left < right - 1:
            mid = left + ((right - left) // 2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle scenario #1 #2
        return left if nums[left] >= nums[right] else right
