# Problem Statement
# Given a set with distinct elements, find all of its distinct subsets.

def find_subsets(nums):
    """
    Time: O(2n)
    Space: O(2n)
    """
    subsets = [[]]
    # start by adding the empty subset
    for num in nums:
        for i in range(len(subsets)):  # we will take all existing subsets and insert the current number in them to
            subsets.append(subsets[i] + [num])  # create a new subset from the existing subset and insert the current
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
