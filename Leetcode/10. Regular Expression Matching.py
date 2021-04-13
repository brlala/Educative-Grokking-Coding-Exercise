class Solution:
    def isMatch(self, s, p):
        memo = {}
        return self.dfs(s, p, memo)

    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]
        if not p:  # if pattern finish and still have string, or string finish but still have pattern
            return not s
        if p[-1] == '*':
            if self.dfs(s, p[:-2], memo):  # try matching in case of repeated cahracters like s: aaaab, p: aaa*b, this is also a base case for when s is consumed s:'', p:'*a'
                memo[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.dfs(s[:-1], p, memo):
                # character match or wild character
                memo[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.dfs(s[:-1], p[:-1], memo):
            memo[(s, p)] = True
            return True
        memo[(s, p)] = False
        return False


a = Solution()
# a.isMatch('aa', 'a')
# a.isMatch('aa', 'a*')
# print(a.isMatch('ab', '.*'))
# print(a.isMatch('aab', 'c*a*b*'))
# print(a.isMatch("mississippi", "mis*is*ip*."))
# print(a.isMatch("ab",".*c"))
# print(a.isMatch("aaa", "aaaa"))
print(a.isMatch("aaaaa", "aa*a"))  # test this case
