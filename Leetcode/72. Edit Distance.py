class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Naive recursing
        """
        if not word1 and not word2:
            return 0
        elif not word1 and word2:
            return len(word2)
        elif not word2 and word1:
            return len(word1)
        elif word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        insert = 1 + self.minDistance(word1, word2[1:])
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(delete, insert, replace)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        memoized solution, NOT WORKING
        """

        def helper(w1, w2):
            if not word1 and not word2:
                return 0
            elif not word1:
                return len(word2)
            elif not word2:
                return len(word1)

            if (w1, w2) not in memo:
                if word1[0] == word2[0]:
                    res = self.minDistance(word1[1:], word2[1:])
                else:
                    delete = 1 + self.minDistance(word1[1:], word2)
                    insert = 1 + self.minDistance(word1, word2[1:])
                    replace = 1 + self.minDistance(word1[1:], word2[1:])
                    res = min(delete, insert, replace)
                memo[(w1, w2)] = res
            return memo[(w1, w2)]

        memo = {}
        return helper(word1, word2)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        https://www.youtube.com/watch?v=MiqoA-yF-0M
        https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
        DP solution
         '' r o s
       ''|0|1|2|3|
        h|1| | | |
        o|2| | | |
        r|3| | | |
        s|4| | | |
        e|5| | | |
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # m is go down, n is go right
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]