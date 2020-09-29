# Problem Statement
# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the
# array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array
# can have duplicates.

def binary_search(arr, key):
    """
    Time: O(logN)
    Space: O(1)
    """
    start, end = 0, len(arr) - 1
    is_ascending = arr[-1] > arr[0]
    while start <= end:
        # calculate middle of current range
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid

        if is_ascending:
            if key < arr[mid]:
                end = mid - 1  # key can be first half
            else:
                start = mid + 1  # key will be in second half
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([10, 6, 4], 10))
print(binary_search([10, 6, 4], 4))
