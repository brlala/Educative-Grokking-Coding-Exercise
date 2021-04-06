class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        ans = self.nums[:]
        for i in range(len(ans)):
            j = random.randrange(i + 1)
            # nums = [x1, x2, x3, ..., xn]
            # new = []
            # Choose 1st number with probablity 1/len(nums)
            # Remove this number and add to new.
            # Choose 2nd number with probablity 1/(len(nums) - 1)
            # Remove this number and add to new

            # So, P = P(choose 1st num from n) x P(choose 2nd from n - 1) x P(choose 3rd from n - 2) x ... x P(choose nth from 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()