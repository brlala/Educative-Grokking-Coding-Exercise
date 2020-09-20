# Problem Statement
#

def search_quadruplets(arr, target_sum):
    """
    Time:
    Space:
    """
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        # skip same element to avoid duplicate quadruplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            search_pairs(arr, target_sum, i, j, quadruplets)
    return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        current_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if current_sum == target_sum:
            quadruplets.append((arr[first], arr[second], arr[left], arr[right]))
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right-1]:
                right -= 1

        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1


print(search_quadruplets([4, 1, 2, -1, 1, -3], 1) == [(-3, -1, 1, 4), (-3, 1, 1, 2)])
print(search_quadruplets([2, 0, -1, 1, -2, 2], 2) == [(-2, 0, 2, 2), (-1, 0, 1, 2)])
