class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        https://leetcode.com/problems/word-break-ii/discuss/44368/Python-easy-to-understand-solutions-(memorization%2BDFS-DP%2BDFS)
        """
        memo = {}
        return self.dfs(s, set(wordDict), memo)

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                for word in self.dfs(s[i:], wordDict, memo):
                    res.append(s[:i] + (" " if word else "") + word)
        memo[s] = res
        return res

