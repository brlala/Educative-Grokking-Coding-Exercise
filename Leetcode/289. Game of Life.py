class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy
        row = len(board)
        col = len(board[0])
        oriBoard = copy.deepcopy(board)
        for i in range(row):
            for j in range(col):
                neigh_count = {}
                neigh_count[0] = neigh_count[1] = 0
                self.getSurrounding(oriBoard, (i, j), neigh_count)
                board[i][j] = self.getState(oriBoard[i][j], neigh_count)

    def getSurrounding(self, board, loc, neigh_count):
        row, col = loc
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                elif 0 <= i < len(board) and 0 <= j < len(board[0]):
                    neigh_count[board[i][j]] += 1

    def getState(self, current, neigh_count):
        if current ==0 and neigh_count[1] == 3:
            return 1
        elif neigh_count[1] < 2:
            return 0
        elif neigh_count[1] > 3:
            return 0
        elif neigh_count[1] == 2 or neigh_count[1] == 3:
            return current
        else:
            return 1


a = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
a.gameOfLife(board)
print(board)
