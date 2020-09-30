# Problem Statement
# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a
# given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You
# can assume that the given array does not have any duplicates.


def count_rotations(arr):
    """
    Time: O(logN)
    Space: O(1)
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = int(start + (end - start) // 2)
        # if mid is greater than next element
        if mid < end and arr[mid] > arr[mid+1]:
            return mid + 1

        # if mid is smaller than previous element:
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # this is the only difference from the previous solution
        # if numbers at indices start, mid, and end are same, we can't choose a side
        # the best we can do is to skip one number from both ends if they are not the
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:  # if element at start+1 is not the smallest
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:  # if the element at end is not the smallest
                return end
            end -= 1
        # left side is sorted, so the pivot is on right side
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:  # right side is sorted in ascending order so pivot is at left side
            end = mid - 1
    return 0


# print(count_rotations([10, 15, 1, 3, 8]))
# print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
# print(count_rotations([1, 3, 8, 10]))
print(count_rotations([3, 3, 4, 5, 6, 7, 3, 3, 3]))

