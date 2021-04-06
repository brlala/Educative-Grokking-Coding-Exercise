import collections


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r = len(s1)
        c = len(s2)
        l = len(s3)
        if r + c != l:
            return False

        queue = collections.deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            x, y = queue.popleft()
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                visited.add((x + 1, y))
                queue.append((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                visited.add((x, y + 1))
                queue.append((x, y + 1))
        return False


a = Solution()
a.isInterleave("aabcc", "dbbca", "aadbbcbcac")
a.isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
               "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
               "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb")
