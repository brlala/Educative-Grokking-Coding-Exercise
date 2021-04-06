class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = collections.defaultdict(int)
        p_counter = collections.defaultdict(int)
        for char in p:
            p_counter[char] += 1
        for char in s[:len(p) - 1]:
            s_counter[char] += 1

        len_p = len(p)
        len_s = len(s)
        res = []
        for i in range(len_p - 1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                res.append(i - len_p + 1)
            s_counter[s[i - len_p + 1]] -= 1
            if s_counter[s[i - len_p + 1]] == 0:
                del s_counter[s[i - len_p + 1]]
        return res
