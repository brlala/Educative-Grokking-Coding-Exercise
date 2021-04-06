class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        count = 0
        toCheck = {n}
        visited = set()
        while toCheck:
            count += 1
            temp = set()
            for x in toCheck:
                if x in visited:
                    continue
                else:
                    visited.add(x)
                for y in lst:
                    if x == y:
                        return count
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp
        return count


a = Solution()
print(a.numSquares(3))
