class Solution:
    def lexicalOrder(self, n):
        """
        https://leetcode.com/problems/lexicographical-numbers/discuss/86240/How-to-think-it-in-the-DFS-way
        """

        def dfs(res, k):
            if k <= n:
                res.append(k)
                t = 10 * k
                if t <= n:
                    for i in range(10):
                        dfs(res, t + i)

        res = []
        for i in range(1, 10):
            dfs(res, i)
        return res

    def lexicalOrder(self, n):
        """
        Cheating using str
        """
        res = [i for i in range(1, n + 1)]
        res.sort(key=str)
        return res
