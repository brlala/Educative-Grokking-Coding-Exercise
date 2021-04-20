# Given a chemical formula (given as a string), return the count of each atom. The atomic element always starts with
# an uppercase character, then zero or more lowercase letters, representing the name. One or more digits representing
# that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For
# example, H2O and H2O2 are possible, but H1O2 is impossible. Two formulas concatenated together to produce another
# formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3
# are formulas. Given a formula, return the count of all elements as a string in the following form: the first name (
# in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted
# order), followed by its count (if that count is more than 1), and so on.
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        https://leetcode.com/problems/number-of-atoms/discuss/162066/Python%3A-with-stack-and-dict-at-O(-nlog)-solution
        """
        # 12:33pm
        # 1:10pm

        stack = [1]
        index = len(formula) - 1
        nums_str = ''
        num = 1

        element = ''
        atoms_count = defaultdict(int)
        # possible cases, number, alphabet, bracket
        while index >= 0:
            # get all numbers
            while '0' <= formula[index] <= '9':
                nums_str = formula[index] + nums_str
                index -= 1

            if nums_str != '':
                num = int(nums_str)

            if formula[index] == ')':
                stack.append(stack[-1] * num)
            elif 'a' <= formula[index] <= 'z' or 'A' <= formula[index] <= 'Z':
                while 'a' <= formula[index] <= 'z':
                    element = formula[index] + element
                    index -= 1
                element = formula[index] + element
                atoms_count[element] += num*stack[-1]
            else:
                stack.pop()
            nums_str = ''
            num = 1
            element = ''
            index -= 1

        res = [f"{k}{v}" if v > 1 else k for k, v in atoms_count.items()]
        res.sort()
        return ''.join(res)

a = Solution()
a.countOfAtoms("Be32")
