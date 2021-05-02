class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Brute force method O(n^2)
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                concat_words = words[i] + words[j]
                if concat_words == concat_words[::-1]:
                    res.append((i, j))
        return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        optimized O(N*k^2), iterate over all words, iterate over all characters, check palindrome
        4 different cases:
        Case 1: If s2 is the reversing string of s1, then s1+s2 and s2+s1 are palindrome.
        Case 2: If s1 is a blank string, then for any string that is palindrome s2, s1+s2 and s2+s1 are palindrome.
        Case 3: If s1[0:cut] is palindrome and there exists s2 is the reversing string of s1[cut+1:] , then s2+s1 is palindrome.
        Case 4: Similiar to case3. If s1[cut+1: ] is palindrome and there exists s2 is the reversing string of s1[0:cut] , then s1+s2 is palindrome.
        # code:
        # reference: https://leetcode.com/problems/palindrome-pairs/discuss/79210/The-Easy-to-unserstand-JAVA-Solution

        """
        d = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            # no divide
            # case 1: append palindrome with palindrome ['abcd', 'dbca']
            if w[::-1] in d and d[w[::-1]] != i:
                res.append([i, d[w[::-1]]])
            # case 2: append all palindrome with empty ['tot', '']
            if w != '' and w[::-1] == w and '' in d:
                res.append([i, d['']])
                res.append([d[''], i])

            # divided into two parts
            # case 3: need to concat to form palindromic ['lls', 's']
            for k in range(1, len(w)):
                s1, s2 = w[:k], w[k:]  # s1=l, s2=ls, check if ls in d
                if s1 == s1[::-1] and s2[::-1] in d:
                    res.append([d[s2[::-1]], i])  #same as case 3
                if s2 == s2[::-1] and s1[::-1] in d:
                    res.append([i, d[s1[::-1]]])
        return res