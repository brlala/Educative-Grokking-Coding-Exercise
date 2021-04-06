class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        for i in range(0, self.m):
            self.dfs(i, 0)
            self.dfs(i, self.n - 1)

        for j in range(0, self.n):
            self.dfs(0, j)
            self.dfs(self.m - 1, j)

        for i in range(self.m):
            for j in range(self.n):
                board[i][j] = 'X' if board[i][j] != 'T' else 'O'

    def dfs(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n and self.board[i][j] == 'O':
            self.board[i][j] = 'T'
            self.dfs(i - 1, j)
            self.dfs(i + 1, j)
            self.dfs(i, j - 1)
            self.dfs(i, j + 1)

a = Solution()