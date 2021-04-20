class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
        """
        string_list = list(s)
        stack = []
        # first round, replace additional ')'
        for idx, c in enumerate(string_list):
            if c == '(':
                stack.append(idx)
            elif c == ')':
                if not stack:
                    string_list[idx] = ''
                else:
                    stack.pop()

        # second round, replace all '(' thatdoesn't match
        while stack:
            string_list[stack.pop()] = ''

        return ''.join(string_list)
