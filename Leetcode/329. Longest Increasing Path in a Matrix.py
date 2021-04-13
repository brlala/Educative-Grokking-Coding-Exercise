class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """
        DFS
        """

        def traverse_longest(row, col, prev_num):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            current_num = matrix[row][col]
            if current_num <= prev_num:
                return 0
            up = traverse_longest(row - 1, col, current_num)
            down = traverse_longest(row + 1, col, current_num)
            left = traverse_longest(row, col - 1, current_num)
            right = traverse_longest(row, col + 1, current_num)
            return 1 + max(up, down, left, right)

        max_longest = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                max_longest = max(traverse_longest(i, j, float('-inf')), max_longest)
        return max_longest

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        memoization
        """
        self.max_longest = 0

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                up = dfs(i - 1, j) if i and val < matrix[i - 1][j] else 0
                left = dfs(i, j - 1) if j and val < matrix[i][j - 1] else 0
                down = dfs(i + 1, j) if i < m - 1 and val < matrix[i + 1][j] else 0
                right = dfs(i, j + 1) if j < n - 1 and val < matrix[i][j + 1] else 0
                dp[i][j] = 1 + max(up, down, left, right)
                self.max_longest = max(self.max_longest, dp[i][j])
            return dp[i][j]

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return self.max_longest


a = Solution()
print(a.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(a.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
