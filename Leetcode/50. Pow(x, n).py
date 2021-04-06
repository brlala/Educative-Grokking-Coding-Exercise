class Solution(object):
    def myPow(self, a, b):
        """
        https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
        if is even, directly multiple, if it is odd, multiply a by one more time.
        """
        if b < 0:
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)

    def helper(self, a, b):
        if b == 0: return 1
        half = self.helper(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a