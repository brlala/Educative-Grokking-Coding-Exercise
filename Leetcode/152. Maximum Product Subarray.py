class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Alternative to Kadane's algorithm
        https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
        """
        A = nums[:]
        B = nums[::-1]
        for i in range(1, len(nums)):
            A[i] = A[i] * (A[i - 1] or 1)
            B[i] = B[i] * (B[i - 1] or 1)
        return max(A + B)

    def maxProduct(self, nums: List[int]) -> int:
        """
        Two passes
        https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99
        """
        max_prod = float("-inf")
        product = 1
        for n in nums:
            product *= n
            max_prod = max(product, max_prod)
            if n == 0:
                product = 1

        product = 1
        for n in nums[::-1]:
            product *= n
            max_prod = max(product, max_prod)
            if n == 0:
                product = 1
        return max_prod