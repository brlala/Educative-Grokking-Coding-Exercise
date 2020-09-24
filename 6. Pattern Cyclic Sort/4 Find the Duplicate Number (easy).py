# Problem Statement
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one
# duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You
# are, however, allowed to modify the input array.

def find_duplicate(nums):
    """
    Time: O(N)
    Space: O(1)
    """
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1


print(find_duplicate([1, 4, 4, 3, 2]) == 4)
print(find_duplicate([2, 1, 3, 3, 5, 4]) == 3)
print(find_duplicate([2, 4, 1, 4, 4]) == 4)
