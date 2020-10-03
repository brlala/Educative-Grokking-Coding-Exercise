# Problem Statement
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one
# duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You
# are, however, allowed to modify the input array.

def find_corrupt_numbers(nums):
    """
    Time:
    Space:
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i, num in enumerate(nums):
        if num != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]


print(find_corrupt_numbers([3, 1, 2, 5, 2]) == [2, 4])
print(find_corrupt_numbers([1, 1, 2, 3, 6, 5]) == [1, 4])
