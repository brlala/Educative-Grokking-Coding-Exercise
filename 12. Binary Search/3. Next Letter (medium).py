# Problem Statement
# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater
# than a given ‘key’.
#
# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the
# first letter. This also means that the smallest letter in the given array is greater than the last letter of the
# array and is also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.

def search_next_letter(letters, key):
    """
    Time: O(logN)
    Space: O(1)
    """
    if key < letters[0] or key > letters[-1]:
        return letters[0]

    start, end = 0, len(letters) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # since start<= end, the final iteration will be start==end+1, we are not able to find hence the next big number
    # will just be start
    return letters[start % len(letters)]  # use end if it is to find the floor


print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
