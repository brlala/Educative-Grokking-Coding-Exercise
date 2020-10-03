# Problem Statement
# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’
# numbers out of the total ‘n+1’ numbers, find the missing number.

def find_missing_numbers(nums):
    """
    Time: O(n)
    Space: O(1)
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        # while value less than length, ignore those that are out of array length
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_nums = []
    for i, num in enumerate(nums):
        if num != i + 1:
            missing_nums.append(i + 1)
    return missing_nums


print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7])
print(find_missing_numbers([2, 4, 1, 2]) == [3])
print(find_missing_numbers([2, 3, 2, 1]) == [4])
