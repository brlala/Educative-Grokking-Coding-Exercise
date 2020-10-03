# Problem Statement
# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
# hence, we can’t count 0s, 1s, and 2s to recreate the array.
#
# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists
# of three different numbers that is why it is called Dutch National Flag problem.

def dutch_flag_sort(arr):
    """
    Time:
    Space:
    """
    n = len(arr)
    left, right = 0, n - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
        if arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1
        print(arr)
    return arr


print(dutch_flag_sort([1, 0, 2, 1, 0]) == [0, 0, 1, 1, 2])
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2])
