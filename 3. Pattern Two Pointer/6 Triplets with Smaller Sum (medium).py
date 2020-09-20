# Problem Statement
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the
# target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum
# of the triplet with the smallest sum.

def triplets_with_smaller_sum(arr, target):
    """
    Time: O(N∗logN+N^2)
    Space: O(N) for sorting
    """
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum >= target:
                right -= 1
            else:
                count += (right-left)
                left += 1
    return count


print(triplets_with_smaller_sum([-1, 0, 2, 3], 3) == 2)
print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5) == 4)
