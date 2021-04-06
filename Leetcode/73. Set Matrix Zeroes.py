class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        rowHasZero = not all(matrix[0])
        colHasZero = not all(list(zip(*matrix))[0])
        m = len(matrix)
        n = len(matrix[0])

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if rowHasZero:
            for c in range(n):
                matrix[0][c] = 0

        if colHasZero:
            for r in range(m):
                matrix[r][0] = 0
