# Problem Statement
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

def shortest_window_sort(arr):
    """
    Time:
    Space:
    """
    if not arr:
        return 0
    left, right = 0, len(arr) - 1
    # finding the left
    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1

    if left == len(arr) - 1:
        return 0

    # finding the right
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    subarray_max = max(arr[left:right])
    subarray_min = min(arr[left:right])

    # extend subarray to include number
    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < subarray_max:
        right += 1
    return right - left + 1


print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]) == 5)
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]) == 5)
print(shortest_window_sort([1, 2, 3]) == 0)
print(shortest_window_sort([3, 2, 1]) == 3)
