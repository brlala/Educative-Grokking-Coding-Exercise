# Problem Statement
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

def make_squares(arr):
    """
    Time: O(N) loop through once
    Space: O(N) creating a square array
    """
    n = len(arr)
    squares = [0] * n
    highest_square_index = n - 1
    left, right = 0, n - 1
    while left <= right:
        left_square = arr[left]**2
        right_square = arr[right]**2
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
            highest_square_index -= 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
            highest_square_index -= 1
    return squares


print(make_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
print(make_squares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])
