# We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b",
# ...) are keys, and ("A", "B", ...) are locks.
#
# We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We
# cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a
# lock unless we have the corresponding key.
#
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English
# alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also
# that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.
# Input: ["@.a.#","###.#","b.A.B"]
# Output: 8
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        https://leetcode.com/problems/shortest-path-to-get-all-keys/discuss/364604/Simple-Python-BFS-Solution-(292-ms-beat-97.78)
        """
        rows = len(grid)
        cols = len(grid[0])

        # 1. find the start point
        # 2. find how many key we need to collect
        key_needed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = [r, c]
                if grid[r][c] in 'abcdef':
                    key_needed += 1

        deque = collections.deque([(start[0], start[1], '')])
        seen = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        steps = 0

        while deque:
            size = len(deque)
            for _ in range(size):
                x, y, key = deque.popleft()
                if (x, y, key) in seen:
                    continue
                if len(key) == key_needed:
                    return steps

                seen.add((x, y, key))

                # add possible direction for key
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                        cell = grid[nx][ny]
                        if cell in 'ABCDEF' and cell.lower() in key:
                            deque.append((nx, ny, key))
                        elif cell in '.@':
                            deque.append((nx, ny, key))
                        elif cell in 'abcdef':
                            if cell not in key:
                                deque.append((nx, ny, key + cell))
                            else:
                                deque.append((nx, ny, key))
            steps += 1
        return -1
