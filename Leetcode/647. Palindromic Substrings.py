class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        https://leetcode.com/problems/palindromic-substrings/discuss/153053/647.-Palindromic-Substrings-in-C%2B%2B-and-Java-and-Python
        """
        self.count = 0
        n = len(s)
        for i in range(n):
            self.isPalindrome(s, i, i)  # judge odd length string racecar
            self.isPalindrome(s, i, i + 1)  # judge even length string abba
        return self.count

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.count += 1
            left -= 1
            right += 1
