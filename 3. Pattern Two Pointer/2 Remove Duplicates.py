# Problem Statement
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing
# the duplicates in-place return the new length of the array.

def remove_duplicates(arr):
    """
    Time: O(n)
    Space: O(1) modify list in place
    """
    write_pointer = 0
    for current_pointer, num in enumerate(arr[1:], 1):
        if num != arr[write_pointer]:
            write_pointer += 1
            arr[write_pointer] = num
    return write_pointer + 1


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4)
print(remove_duplicates([2, 2, 2, 11]) == 2)
