class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, path: list, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for idx, num in enumerate(candidates):
            self.dfs(candidates[idx:], target - num, path + [num], res)

