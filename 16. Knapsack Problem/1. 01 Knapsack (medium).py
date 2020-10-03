# Problem Statement
#

def solve_knapsack(profits, weights, capacity):
    """
    Time:
    Space:
    """
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, remaining_capacity, current_index):
    # base case
    if remaining_capacity <= 0 or current_index >= len(profits):
        return 0
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at current_index exceeds the capacity we shouldn't process it
    profit1 = 0
    if weights[current_index] <= remaining_capacity:
        profit1 = profits[current_index] + knapsack_recursive(profits, weights, remaining_capacity - weights[current_index], current_index + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, remaining_capacity, current_index + 1)

    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
