# Problem Statement
# Given a set of distinct numbers, find all of its permutations.
from collections import deque


def diff_ways_to_evaluate_expression(expression):
    result = []
    # base case: if the string is a number, parse and append
    if '+' not in expression and '-' not in expression and '*' not in expression:
        result.append(int(expression))
    else:
        for i in range(len(expression)):
            char = expression[i]
            if not char.isdigit():
                # break the equation into left and right and make recursive calls
                left_parts = diff_ways_to_evaluate_expression(expression[:i])
                right_parts = diff_ways_to_evaluate_expression(expression[i+1:])
                for part1 in left_parts:
                    for part2 in right_parts:
                        if char == '+':
                            result.append(part1+part2)
                        elif char == '-':
                            result.append(part1-part2)
                        elif char == '*':
                            result.append(part1*part2)
    return result


def main():
    print("Different ways of evaluating are: " + str(diff_ways_to_evaluate_expression("1+2*3")))
    print("Different ways of evaluating are: " + str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
