class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Recursive
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)

    def longestSubstring(self, s: str, k: int) -> int:
        """
        Iterative
        """
        ans = 0
        stack = [s]
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))

        return ans

a = Solution()
# a.longestSubstring("aaaaaaaaaaaaaaaaaaccccccccbbddddddddddvvddddddddeee", 3)
a.longestSubstring("ababacb", 3)