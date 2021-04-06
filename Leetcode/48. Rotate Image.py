from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        print(matrix)
        self.mirror(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def mirror(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        doing it in 1 pass
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 0, 0 -> -1, 0 -> -1,-1 -> 0, -1
                # 1, 1 -> -2, 1 -> -2,-2 -> 1, -2
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
