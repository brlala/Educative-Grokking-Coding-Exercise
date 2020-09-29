# Problem Statement
# Given a set of distinct numbers, find all of its permutations.

def find_permutations(nums):
    """
    Time:
    Space:
    """
    result = []
    find_permutations_recursive(nums, 0, [], result)
    return result


def find_permutations_recursive(nums, index, current_permutation, result):
    """
    Time:
    Space:
    """
    if index == len(nums):
        result.append(current_permutation)
    else:
        # create a new permutation by adding the current number at every position
        for i in range(len(current_permutation) + 1):
            new_permutation = list(current_permutation)
            new_permutation.insert(i, nums[index])
            find_permutations_recursive(nums, index + 1, new_permutation, result)


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
