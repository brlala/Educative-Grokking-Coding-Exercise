class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        move one number n times
        Time complexity (k*n)
        """
        n = len(nums)
        k = k % n
        for _ in range(k):
            previous = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            nums[0] = previous

    def rotate(self, nums: List[int], k: int) -> None:
        """
        clever method
        Time complexity O(2n)
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        # nums.reverse()
        # self.reverse(nums, 0, k - 1)
        # self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
