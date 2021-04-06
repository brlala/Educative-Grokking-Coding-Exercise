class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        iterative
        """
        seen = set()
        q = collections.deque([s])
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "":
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        DP programming
        """
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] = dp[i] or dp[i - len(word)]
        return dp[-1]


a = Solution()
a.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
