import bisect
import random


class Solution:
    """
    https://leetcode.com/problems/random-pick-with-weight/discuss/671921/Python-3-simple-solution
    O (
    """
    def __init__(self, w: list[int]):
        self.prob_list = []
        temp = 0
        # produce a probability array [1, 4, 8 , 10, 25]
        for i in w:
            self.prob_list.append(temp + i)
            temp += i
        self.sum = temp

    def pickIndex(self) -> int:
        pr = random.random() * self.sum
        pr = random.randrange(1, self.sum + 1)
        pr = random.randint(1, self.sum)
        return bisect.bisect_left(self.prob_list, pr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

a = Solution([1, 3, 4])
