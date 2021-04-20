class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        DFS
        """

        def dfs(ss):
            nonlocal count
            if not ss:
                count += 1
                return
            for i in range(1, len(ss) + 1):
                substring = ss[:i]
                if substring and not substring.startswith('0') and 1 <= int(substring) <= k:
                    dfs(ss[i:])
            return

        count = 0
        dfs(s)
        return count % 1000000007

    def numberOfArrays(self, s: str, k: int) -> int:
        """
        https://leetcode.com/problems/restore-the-array/discuss/585553/Python-DP-O(len(s)-*-10)-clean-code-with-explanations.
        O(len(s) * 10)
        """
        n = len(s)
        t = len(str(k))
        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1
        for i in range(1, n):
            for j in range(t):
                if i - j >= 0 and 1 <= int(s[i - j:i + 1]) <= k and s[i - j:i + 1][0] != "0":
                    count[i + 1] += count[i - j]
        return count[-1] % 1000000007


a = Solution()
# print(a.numberOfArrays('1000', 10000))
print(a.numberOfArrays('1000', 10))
# print(a.numberOfArrays('1317', 2000))
# print(a.numberOfArrays('2020', 30))
