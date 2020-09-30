# Problem Statement
# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum
# difference with the given ‘key’.


def search_bitonic_array(arr, key):
    """
    Time: O(logN)
    Space: O(1)
    """
    max_index = find_binary_max(arr)
    key_index = binary_search(arr, key, 0, max_index)
    if key_index != -1:
        return key_index
    return binary_search(arr, key, max_index + 1, len(arr) - 1)


def find_binary_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


def binary_search(arr, key, start, end):
    while start <= end:
        mid = int(start + (end - start) / 2)
        if key == arr[mid]:
            return mid
        if arr[start] < arr[end]:  # ascending order
            if key < arr[mid]:
                end = mid - 1
            else:  # key > arr[mid]
                start = mid + 1
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1
            else:  # key < arr[mid]
                start = mid + 1
    return -1  # element is not found


print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([1, 3, 8, 4, 3], 4))
