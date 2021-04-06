# Problem Statement
# Given a set of distinct numbers, find all of its permutations.
from collections import deque


def generate_valid_parentheses(n, open=0):
    """
    Time: O(N * 2^n) convert to char + 2n possible combinations
    Space: O(N * 2^n)
    """
    if n > 0 <= open:
        return ['(' + p for p in generate_valid_parentheses(n-1, open+1)] + \
               [')' + p for p in generate_valid_parentheses(n, open-1)]
    return [')' * open] * (not n)


class ParenthesesString:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count

def generate_valid_parentheses(num):
    """
    Time: O(N * 2^n) convert to char + 2n possible combinations
    Space: O(N * 2^n)
    """
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        # if we've reached the maxumum number of open and close, add to the result
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:  # if we can add open parentheses add it
                queue.append(ParenthesesString(ps.str + "(", ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:  # if we can add close parentheses, add it
                queue.append(ParenthesesString(ps.str + ')', ps.open_count, ps.close_count + 1))
    return result


def generate_valid_parentheses1(num):
    """
    Time: O(N * 2^n) convert to char + 2n possible combinations
    Space: O(N * 2^n)
    """
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(ParenthesesString(ps.str + '(', ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:
                queue.append(ParenthesesString(ps.str + ')', ps.open_count, ps.close_count + 1))
    return result


def main():
    print("String permutations are: " + str(generate_valid_parentheses(2)))
    print("String permutations are: " + str(generate_valid_parentheses(3)))
    print("String permutations are: " + str(generate_valid_parentheses1(2)))
    print("String permutations are: " + str(generate_valid_parentheses1(4)))


main()
