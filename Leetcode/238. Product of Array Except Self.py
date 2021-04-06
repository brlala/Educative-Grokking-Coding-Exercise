class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://www.youtube.com/watch?v=tSRFtR3pv74
        :param nums:
        :return:
        """
        if not nums:
            return False
        arr = [1] * len(nums)
        p1 = p2 = 1
        for i in range(len(nums)):
            arr[i] *= p1
            arr[~i] *= p2
            p1 *= nums[i]
            p2 *= nums[~i]
        return arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Numbers [1 2 3 4 5]
        Pass 1: [- 1 12 123 1234]
        Pass 2: [2345 345 45 5 -]
        """
        if not nums:
            return False
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
