class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix: return
        dir_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        seen = set()
        row = 0
        col = -1

        m = len(matrix)
        n = len(matrix[0])
        res = []
        for _ in range(m * n):
            offset = dir_arr[direction % 4]
            new_row, new_col = row + offset[0], col + offset[1]
            if (new_row, new_col) in seen or new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                direction += 1
            offset = dir_arr[direction % 4]
            new_row, new_col = row + offset[0], col + offset[1]
            val = matrix[new_row][new_col]
            seen.add((new_row, new_col))
            res.append(val)
            row, col = new_row, new_col
        return res

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Peeling off layer one by one (code golfing but not optimal)
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])


a = Solution()
a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
