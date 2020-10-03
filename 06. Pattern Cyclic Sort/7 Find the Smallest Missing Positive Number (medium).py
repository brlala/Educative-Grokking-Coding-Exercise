# Problem Statement
# Given an unsorted array containing numbers, find the smallest missing positive number in it.

def find_first_missing_positive(nums):
    """
    Time:
    Space:
    """
    i = 0
    n = len(nums)
    while i < len(nums):
        j = nums[i] - 1
        # ignoring those out of arrays and negative
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1


print(find_first_missing_positive([-3, 1, 5, 4, 2]) == 3)
print(find_first_missing_positive([3, -2, 0, 1, 2]) == 4)
print(find_first_missing_positive([3, 2, 5, 1]) == 4)
