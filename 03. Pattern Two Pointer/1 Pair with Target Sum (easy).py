# Problem Statement
#

def pair_with_targetsum(arr, target_sum):
    """
    Using dictionary approach
    Time: O(N)
    Space: O(N)
    """
    nums_map = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums_map:
            return [nums_map[target_sum - num], i]
        else:
            nums_map[num] = i
    return None


def pair_with_targetsum(arr, target_sum):
    """
    Using dictionary approach
    Time: O(N)
    Space: O(N)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if target_sum == current_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return None

print(pair_with_targetsum([1, 2, 3, 4, 6], 6) == [1, 3])
print(pair_with_targetsum([2, 5, 9, 11], 11) == [0, 2])
