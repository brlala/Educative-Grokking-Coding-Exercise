# Problem Statement
# Given an unsorted array containing numbers, find the smallest missing positive number in it.

def find_first_k_missing_positive(nums, k):
    """
    Time:
    Space:
    """
    i = 0
    n = len(nums)
    while i < len(nums):
        j = nums[i] - 1
        # ignoring those out of arrays
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()
    for i, num in enumerate(nums):
        if len(missing_numbers) < k:
            if num != i + 1:
                missing_numbers.append(i+1)
                extra_numbers.add(num)

    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        i += 1

    return missing_numbers


print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3) == [1, 2, 6])
print(find_first_k_missing_positive([2, 3, 4], 3) == [1, 5, 6])
print(find_first_k_missing_positive([-2, -3, 4], 2) == [1, 2])
