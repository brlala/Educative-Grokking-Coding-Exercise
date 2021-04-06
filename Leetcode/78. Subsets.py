class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for n in nums:
            res += [item + [n] for item in res]
        return res

    # dfs
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.helper(nums[i+1:], path+[nums[i]], res)


nums = [1, 2, 3]
a = Solution()
print(a.subsets(nums))
