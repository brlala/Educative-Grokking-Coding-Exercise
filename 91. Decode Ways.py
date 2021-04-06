from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.dfs(s)

    @lru_cache
    def dfs(self, s):
        if s and s[0] == '0':
            return 0
        if s == '' or len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            left = self.dfs(s[1:])
            right = self.dfs(s[2:])
            return left + right
        else:
            left = self.dfs(s[1:])
            return left

a = Solution()
a.numDecodings('222')