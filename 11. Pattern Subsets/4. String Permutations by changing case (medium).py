# Problem Statement
# Given a set of distinct numbers, find all of its permutations.


def find_letter_case_string_permutations(string):
    """
    Time: O(N * 2^n) convert to char + 2n possible combinations
    Space: O(N * 2^n)
    """
    permutations = [string]
    for index, char in enumerate(string):
        if char.isalpha():  # only process characters, skip digits
            # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[index] = chs[index].swapcase()
                permutations.append(''.join(chs))
    return permutations


def main():
    print("String permutations are: " + str(find_letter_case_string_permutations('ad52')))
    print("String permutations are: " + str(find_letter_case_string_permutations('ab7c')))


main()
