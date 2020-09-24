# Problem Statement
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some duplicates,
# find all the duplicate numbers without using any extra space.

def find_duplicate(nums):
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

    duplicate_numbers = []
    for i, num in enumerate(nums):
        if num != i + 1:
            duplicate_numbers.append(num)
    return duplicate_numbers


print(find_duplicate([3, 4, 4, 5, 5]) == [5, 4])
print(find_duplicate([5, 4, 7, 2, 3, 5, 3]) == [3, 5])
