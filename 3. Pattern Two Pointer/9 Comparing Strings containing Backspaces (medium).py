# Problem Statement
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

def get_next_valid_character(string, index):
    backspace = 0
    while string[index] == '#':
        backspace += 1
        index -= 1
    return index - backspace


def backspace_compare(str1, str2):
    """
    Time:
    Space:
    """
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_character(str1, index1)
        i2 = get_next_valid_character(str2, index2)
        if i1 < 0 and i2 < 0:
            return True
        elif i1 < 0 or i2 < 0:
            return False
        elif str1[i1] != str2[i2]:
            return False
        index1 = i1 - 1
        index2 = i2 - 1
    return True


print(backspace_compare("xy#z", "xzz#") is True)
print(backspace_compare("xy#z", "xyz#") is False)
print(backspace_compare("xp#", "xyz##") is True)
print(backspace_compare("xywrrmp", "xywrrmu#p") is True)
