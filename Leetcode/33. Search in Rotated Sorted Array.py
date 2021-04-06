class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 45678 90123 and target in left side
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]: #target in left side
                    right = mid - 1
                else:  # target in right side
                    left = mid + 1
            else:  #7890 123456
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search(self, nums: 'List[int]', target: int) -> int:
        L, H = 0, len(nums) - 1
        while L <= H:
            M = (L+H) // 2
            if nums[M] == target:
                return M
            if target <= nums[0] <= nums[M]: # -inf
                L = M+1
            elif target >= nums[0] >= nums[M]: # +inf
                H = M-1
            elif nums[M] <= target:
                L = M+1
            elif nums[M] >= target:
                H = M-1
        return -1


a = Solution()
print(a.search([5,1,3],
3))
