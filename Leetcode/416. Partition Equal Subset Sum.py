class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        With backtracking, immediate return
        """

        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j + 1, x - nums[j]):
                            memo[x] = True
                            break
            return memo[x]

        s, n, memo = sum(nums), len(nums), {0: True}
        if s % 2: return False
        nums.sort(reverse=True)
        return dfs(0, s / 2)

    def canPartition(self, nums: List[int]) -> bool:
        """
        naive without backtracking
        """

        def dfs(index, target):
            if (index, target) in memo:
                return memo[(index, target)]
            if target == 0:
                return True
            if target < 0 or index >= len(nums):
                return False
            memo[(index, target)] = dfs(index + 1, target) or dfs(index + 1, target - nums[index])
            return memo[(index, target)]

        s = sum(nums)
        if s % 2: return False
        memo = {}
        return dfs(0, s / 2)