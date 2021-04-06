class Solution:
    class Solution:
        def change(self, amount: int, coins: List[int]) -> int:
            """
            DFS
            """
            coins.reverse()

            @lru_cache(maxsize=None)
            def helper(index, remaining):
                if remaining == 0:
                    return 1
                if remaining < 0 or index >= len(coins):
                    return 0
                return helper(index, remaining - coins[index]) + helper(index + 1, remaining)

            return helper(0, amount)

        def change(self, amount: int, coins: List[int]) -> int:
            """
            Dynamic Programming
            """
            dp = [0] * (amount + 1)
            dp[0] = 1
            for i in coins:
                for j in range(i, amount + 1):
                    dp[j] += dp[j - i]
            return dp[amount]


a = Solution()
a.change(5, [1, 2, 5])
