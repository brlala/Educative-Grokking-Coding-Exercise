class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        allowing extra space
        """
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)

    def findDuplicate(self, nums: List[int]) -> int:
        """
        constant space, non mutable array, only works with positive, Floyd's algorithm
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow