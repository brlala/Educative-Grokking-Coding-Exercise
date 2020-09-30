# Problem Statement
# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a
# given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You
# can assume that the given array does not have any duplicates.


def search_rotated_array(arr, key):
    """
    Time: O(logN)
    Space: O(1)
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = int(start + (end - start) // 2)
        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:  # left side is sorted in ascending order
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:  # key > arr[mid]
                start = mid + 1
        else:  # right side is sorted in ascending order
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:  # key < arr[mid]
                end = mid - 1
    return -1


print(search_rotated_array([10, 15, 1, 3, 8], 15))
print(search_rotated_array([0, 1, 2, 3, 4, 5, 7, 9, 10, 11, -2, -1], -1))

