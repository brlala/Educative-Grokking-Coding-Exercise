# Problem Statement
# Given a set with distinct elements, find all of its distinct subsets.

def find_subsets(nums):
    """
    Time:
    Space:
    """
    list.sort(nums)
    subsets = [[]]
    start = end = 0
    for i in range(len(nums)):
        start = 0
        # if current element and previous element is same, create new subsets only from the subsets added in the previous
        # step
        if i > 0 and nums[i] == nums[i-1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            subsets.append(subsets[j] + [nums[i]])  # create a new subset from the existing subset and insert the current
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
