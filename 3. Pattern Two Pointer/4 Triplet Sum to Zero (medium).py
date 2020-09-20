# Problem Statement
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

def search_triplets(arr):
    """
    Time: O(N∗logN+N^2)
    Space: O(N) for sorting
    """
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                triplets.append((arr[i], arr[left], arr[right]))
                # skip same element to avoid duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    print(triplets)
    return triplets

# def search_triplets(arr):
#     """
#     Time:
#     Space:
#     """
#     res = []
#     arr.sort()
#     for i in range(len(arr) - 2):
#         if i > 0 and arr[i] == arr[i - 1]:
#             continue
#         left, right = i + 1, len(arr) - 1
#         while left < right:
#             current_sum = arr[i] + arr[left] + arr[right]
#             if current_sum < 0:
#                 left += 1
#             elif current_sum > 0:
#                 right -= 1
#             else:
#                 res.append((arr[i], arr[left], arr[right]))
#                 while left < right and arr[left] == arr[left + 1]:
#                     left += 1
#                 while left < right and arr[right] == arr[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#     return res

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]) == [(-3, 1, 2), (-2, 0, 2), (-2, 1, 1), (-1, 0, 1)])
print(search_triplets([-5, 2, -1, -2, 3]) == [(-5, 2, 3), (-2, -1, 3)])
