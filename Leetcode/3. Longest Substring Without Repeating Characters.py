class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        right = 0
        max_length = 0
        while left < n and right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                seen.remove(s[left])
                left += 1
        return max_length

