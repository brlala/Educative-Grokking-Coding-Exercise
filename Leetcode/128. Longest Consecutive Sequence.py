class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
        """
        nums = set(nums)
        longest_streak = 0
        for n in nums:
            if n - 1 not in nums:  # this part makes it traverse at most O(mn) because it only goes one direction
                counter = n + 1
                while counter in nums:
                    counter += 1
                longest_streak = max(longest_streak, counter - n)

        return longest_streak
a = Solution()
print(a.longestConsecutive([100,4,200,1,3,2]))
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))