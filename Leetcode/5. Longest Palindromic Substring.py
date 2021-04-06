class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return
        res = ''
        n = len(s)
        index = 0
        for i in range(n):
            tmp = odd_string = self.expandFromMiddle(s, i, i)  # abba
            if len(tmp) > len(res):
                res = tmp
                index = i
            tmp = even_string = self.expandFromMiddle(s, i, i + 1)  # racecar
            if len(tmp) > len(res):
                res = tmp
                index = i
            # shortcut using max
            # res = max(self.expandFromMiddle(s, i, i), self.expandFromMiddle(s, i, i + 1), res, key=len)
        test = s[index-(len(res)-1)//2:index+len(res)//2+1]
        return res

    def expandFromMiddle(self, s, left, right):
        if left > right or not s:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

a = Solution()
a.longestPalindrome("cbabab")
a.longestPalindrome("racecar")
a.longestPalindrome("abbadef")