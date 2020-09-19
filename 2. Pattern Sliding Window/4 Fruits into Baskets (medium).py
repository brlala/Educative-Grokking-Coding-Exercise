# Problem Statement # Given an array of characters where each character represents a fruit tree, you are given two
# baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket
# can have only one type of fruit.
#
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each
# tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.
def fruits_into_basket(fruits: list) -> int:
    """
    Time: O(n+n)
    Space: O(1)
    """
    fruit_frequency = {}
    window_start = max_length = 0
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(fruits_into_basket(['A', 'B', 'C', 'A', 'C']) == 3)
print(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']) == 5)
