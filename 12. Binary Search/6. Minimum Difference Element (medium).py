# Problem Statement
# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum
# difference with the given ‘key’.


def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    elif key > arr[-1]:
        return arr[-1]
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]
    a = key-arr[start]
    b = key-arr[end]
    return arr[start] if a > b else arr[end]


print(search_min_diff_element([4, 6, 10], 7))
print(search_min_diff_element([4, 6, 10], 4))
print(search_min_diff_element([1, 3, 8, 10, 15], 12))
print(search_min_diff_element([4, 6, 10], 17))


