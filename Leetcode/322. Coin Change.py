class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Dynamic programming
        """
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

    # def coinChange(self, coins, amount):
    #     """
    #     DFS
    #     """
    #     coins.sort(reverse=True)
    #     min_coins = float('inf')
    #
    #     def dfs(index, coin_count, remaining):
    #         nonlocal min_coins
    #         if remaining == 0:
    #             min_coins = min(min_coins, coin_count)
    #             return
    #
    #         for i in range(index, len(coins)):
    #             remaining_coin_allowance = min_coins - coin_count
    #             max_amount_possible = coins[i] * remaining_coin_allowance
    #
    #             if coins[i] <= remaining and remaining < max_amount_possible:
    #                 dfs(i, coin_count + 1, remaining - coins[i])
    #
    #     dfs(0, 0, amount)
    #     return min_coins if min_coins < float('inf') else -1

a= Solution()
a.coinChange([1,2,5],11)