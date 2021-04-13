class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99111/Evolve-from-brute-force-to-dp
        Brute force O(2^n)
        """
        left = 0
        right = len(s) - 1
        return self.dfs(left, right, s)

    def dfs(self, left, right, s):
        if left == right:
            return 1
        if left > right:
            return 0
        if s[left] == s[right]:
            return 2 + self.dfs(left + 1, right - 1, s)
        else:
            return max(self.dfs(left + 1, right, s), self.dfs(left, right - 1, s))

    def longestPalindromeSubseq(self, s):
        """
        https://leetcode.com/problems/longest-palindromic-subsequence/discuss/216717/Python-DP-solution-w-explanation
        Use DP
       i'jB B B A B
        B|1| | | | |
        B|-|1| | | |
        B|-|-|1| | |
        A|-|-|-|1| |
        B|-|-|-|-|1|
        BCCCB has a length of 5 that is a palindrome, while CCCB has 3 (CCC)

        Visualization:
        https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution/103142
        """

        str_len = len(s)
        dp_matrix = [[0] * len(s) for i in range(str_len)]

        k = 0
        while k < str_len:
            for i in range(str_len - k):
                j = i + k
                if i == j:
                    dp_matrix[i][j] = 1
                elif s[i] == s[j]:
                    dp_matrix[i][j] = dp_matrix[i + 1][j - 1] + 2
                else:
                    dp_matrix[i][j] = max(dp_matrix[i][j - 1], dp_matrix[i + 1][j])
            k += 1

        return dp_matrix[0][str_len - 1]


a = Solution()
a.longestPalindromeSubseq("BBBAB")
