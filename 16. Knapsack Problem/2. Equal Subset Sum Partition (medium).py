# Problem Statement
#

def can_partition(num):
    s = sum(num)
    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False
    return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, sum, current_index):
    if sum == 0:
        return True

    n = len(num)
    if n == 0 or current_index >= n:
        return False
    # recursive call after choosing the number at the `currentIndex`
    # if the number at `currentIndex` exceeds the sum, we shouldn't process this
    if num[current_index] <= sum:
        if can_partition_recursive(num, sum - num[current_index], current_index + 1):
            return True
    # recursive call after excluding the number at the 'currentIndex'
    return can_partition_recursive(num, sum, current_index + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
