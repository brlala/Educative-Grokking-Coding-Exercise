# Problem Statement
# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’
# based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the
# object with sequence number ‘4’.
#
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra
# space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though
# each number is actually an object.


def cyclic_sort(arr):
    """
    Time: O(n)+O(n−1)
    Space: O(1)
    """
    i = 0
    while i < len(arr):
        # if value-1 not equals to index, swap
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr


print(cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5])
print(cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6])
print(cyclic_sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6])
