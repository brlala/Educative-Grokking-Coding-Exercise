class Solution:
    #     def isValidSudoku(self, board: List[List[str]]) -> bool:
    #         return self.isRowValid(board) and self.isColValid(board) and self.isSquareValid(board)

    #     def isRowValid(self, board):
    #         for row in board:
    #             if not self.isUnitValid(row):
    #                 return False
    #         return True

    #     def isColValid(self, board):
    #         for col in zip(*board):
    #             if not self.isUnitValid(col):
    #                 return False
    #         return True

    #     def isSquareValid(self, board):
    #         for i in (0, 3, 6):
    #             for j in (0, 3, 6):
    #                 square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
    #             if not self.isUnitValid(square):
    #                 return False
    #         return True

    #     def isUnitValid(self, unit):
    #         i = [num for num in unit if num != '.']
    #         return len(set(i)) == len(i)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        This method is faster and make use of dictionary
        """
        big = set()
        for i in range(0, 9):
            for j in range(0, 9):
                current = board[i][j]
                if current != '.':
                    if (i, current) in big or (current, j) in big or (i // 3, j // 3, current) in big:
                        return False
                    big.add((i, current))
                    big.add((current, j))
                    big.add((i // 3, j // 3, current))
        return True