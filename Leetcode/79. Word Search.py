class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                found = self.dfs(board, row, col, word)
                if found:
                    return True
        return False

    def dfs(self, board, row, col, word):
        if not word:
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[0]:
            return False
        val = board[row][col]  # first character is found, check the remaining part
        board[row][col] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, row, col + 1, word[1:]) or \
              self.dfs(board, row + 1, col, word[1:]) or \
              self.dfs(board, row, col - 1, word[1:]) or \
              self.dfs(board, row - 1, col, word[1:])
        board[row][col] = val
        return res

    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        DFS Helper without changing board, using visited set, backtracking
        """
        self.found = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = set()
                self.dfs(board, row, col, word, visited)
                if self.found:
                    return True
        return False

    def dfs(self, board, row, col, word, visited):
        if not word:
            self.found = True
        if not self.found and 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[0] and (
                row, col) not in visited:
            visited.add((row, col))
            self.dfs(board, row, col + 1, word[1:], visited)
            self.dfs(board, row + 1, col, word[1:], visited)
            self.dfs(board, row, col - 1, word[1:], visited)
            self.dfs(board, row - 1, col, word[1:], visited)
            visited.remove((row, col))


a = Solution()
print(a.exist(
    [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
    "ABCEFSADEESE"))
