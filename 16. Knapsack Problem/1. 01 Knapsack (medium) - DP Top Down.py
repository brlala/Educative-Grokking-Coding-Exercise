# Problem Statement
#

def solve_knapsack(profits, weights, capacity):
    """
    Time: O(N∗C), can only have a maximum combination of N*C,‘N’ is the number of items and ‘C’ is the knapsack capacity
    Space: O(N∗C) memoization of array + O(N) for recursion call stack
    """
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    profit = knapsack_recursive(dp, profits, weights, capacity, 0)
    return profit


def knapsack_recursive(dp, profits, weights, remaining_capacity, current_index):
    # base case
    if remaining_capacity <= 0 or current_index >= len(profits):
        return 0

    # if we already solved a similar problem, return the result from memory
    if dp[current_index][remaining_capacity] != -1:
        return dp[current_index][remaining_capacity]
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at current_index exceeds the capacity we shouldn't process it
    profit1 = 0
    if weights[current_index] <= remaining_capacity:
        profit1 = profits[current_index] + knapsack_recursive(dp, profits, weights, remaining_capacity - weights[current_index], current_index + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(dp, profits, weights, remaining_capacity, current_index + 1)

    dp[current_index][remaining_capacity] = max(profit1, profit2)
    return dp[current_index][remaining_capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
