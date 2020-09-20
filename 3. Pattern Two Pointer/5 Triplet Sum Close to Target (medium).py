# Problem Statement
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the
# target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum
# of the triplet with the smallest sum.

def triplet_sum_close_to_target(arr, target_sum):
    """
    Time:
    Space:
    """
    if len(arr) < 3:
        return
    arr.sort()
    result = arr[0] + arr[1] + arr[2]
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return current_sum
            if abs(current_sum - target_sum) < abs(result - target_sum):
                result = current_sum
            if current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
    return result


print(triplet_sum_close_to_target([-2, 0, 1, 2], 2) == 1)
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0)
print(triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3)
