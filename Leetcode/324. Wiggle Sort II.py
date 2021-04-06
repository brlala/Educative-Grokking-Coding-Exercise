class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])  # always wants the bigger half len(nums) - len(nums)//2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        for i in range(0, len(nums), 2): nums[i] = arr.pop()