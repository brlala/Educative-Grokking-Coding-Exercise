class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        dfs
        :param triangle:
        :return:
        """
        if not triangle: return 0
        memo = {}
        return self.helper(triangle, memo, 0, 0)

    def helper(self, triangle, memo, row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        if row == len(triangle) - 1:
            return triangle[row][col]
        left = self.helper(triangle, memo, row + 1, col)
        right = self.helper(triangle, memo, row + 1, col + 1)
        total = triangle[row][col] + min(left, right)
        memo[(row, col)] = total
        return total

    def dyn(self, triangle):
        """
        dynamic programming
        :param triangle:
        :return:
        """
        dp = {(len(triangle) - 1, c): triangle[-1][c] for c in range(len(triangle[-1]))}
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                val = triangle[r][c]
                dp[(r, c)] = min(dp[(r + 1, c)], dp[(r + 1, c + 1)]) + val
        return dp[(0, 0)]

    def dyn_ip(self, triangle):
        """
        dynamic programming + in place
        :param triangle:
        :return:
        """
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c+1])
        return triangle[0][0]


a = Solution()
print(a.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(a.dyn([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(a.dyn_ip([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
