# Problem Statement
# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the
# ‘key’ will be the first and last position of the ‘key’ in the array.
#
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

def find_range(numbers, key):
    """
    Time: O(N)
    Space: O(1)
    """
    start, end = 0, len(numbers) - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if key < numbers[mid]:
            end = mid - 1
        elif key > numbers[mid]:
            start = mid + 1
        else:
            # found key, use sliding window
            start = end = mid
            while start > 0 and numbers[start] == numbers[start - 1]:
                start -= 1
            while end < len(numbers) - 1 and numbers[end] == numbers[end + 1]:
                end += 1
            found = True
            break
    if found:
        return (start, end)
    return (-1, -1)


def find_range(numbers, key):
    """
    Time: O(logN)
    Space: O(1)
    """
    results = [-1, -1]
    results[0] = binary_search(numbers, key, False)
    if results[0] != -1:
        results[1] = binary_search(numbers, key, True)
    return results


def binary_search(arr, key, find_max_index):
    key_index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            key_index = mid
            if find_max_index:
                start = mid + 1
            else:
                end = mid - 1
    return key_index


print(find_range([4, 6, 6, 6, 6, 6, 6, 9], 6))
print(find_range([1, 3, 8, 10, 15], 10))
print(find_range([1, 3, 8, 10, 15], 12))

