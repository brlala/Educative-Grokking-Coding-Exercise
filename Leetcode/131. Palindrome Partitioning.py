class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        self.helper(s, [], res)
        return res

    def helper(self, s, path, res):
        if not s:
            res.append(path[:])
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], path + [s[:i]], res)

    def isPalindrome(self, s):
        return s == s[::-1]


a = Solution()
print(a.partition("aaaaa"))
