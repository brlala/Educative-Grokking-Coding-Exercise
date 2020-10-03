# Problem Statement
#
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def solve_knapsack(profits, weights, capacity):
    """
    Time: O(N∗C), can only have a maximum combination of N*C,‘N’ is the number of items and ‘C’ is the knapsack capacity
    Space: O(N∗C) memoization of array + O(N) for recursion call stack
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != len(profits):
        return 0

    # populate the capacity = 0 columns with '0' capacity we have '0' profits
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for i in range(capacity + 1):
        if i >= weights[0]:
            dp[0][i] = profits[0]

    # process all sub-arrays for all the capacities
    for idx in range(1, n):
        for cap in range(1, capacity + 1):
            profit1 = profit2 = 0
            # include the item if the capacity needed is less
            if weights[idx] <= cap:
                profit1 = profits[idx] + dp[idx - 1][cap - weights[idx]]
            # exclude the item
            profit2 = dp[idx - 1][cap]
            dp[idx][cap] = max(profit1, profit2)
    pp.pprint(dp)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print('Selected weights are: ', end='')
    n = len(weights)
    total_profit = dp[n - 1][capacity]
    for idx in range(n - 1, 0, -1):
        if total_profit != dp[idx - 1][capacity]:
            print(str(weights[idx]), end=' ')
            capacity -= weights[idx]
            total_profit -= profits[idx]
    # to print last element
    if total_profit != 0:
        print(str(weights[0]), end=' ')


def main():
    print("Total knapsack profit: " + str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " + str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
