# slicing
def permute(nums: list[int]) -> list[list[int]]:
    res = []
    permute_helper(nums, [], res)
    return res


def permute_helper(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        permute_helper(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# backtracking
def permute(nums: list[int]) -> list[list[int]]:
    visited = set()
    res = []
    backtracking(res, visited, [], nums)
    return res


def backtracking(res, visited, subset, nums):
    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res, visited, subset+[nums[i]], nums)
            visited.remove(i)


print(permute([1, 2, 3]))
