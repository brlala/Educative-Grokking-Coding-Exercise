class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        self.helper(n, n, [], res)
        return res

    def helper(self, open_parens, close_parens, path, res):
        if not open_parens and not close_parens:
            res.append(''.join(path))
            return
        # append open parens
        if open_parens:
            self.helper(open_parens - 1, close_parens, path + ['('], res)
        if close_parens > open_parens and close_parens:
            self.helper(open_parens, close_parens - 1, path + [')'], res)

a = Solution()
print(a.generateParenthesis(3))