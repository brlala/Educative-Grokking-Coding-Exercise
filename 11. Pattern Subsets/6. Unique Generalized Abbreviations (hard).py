# Problem Statement
# Given a set of distinct numbers, find all of its permutations.
from collections import deque


class AbbreviatedWord:
    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    word_len = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))
    while queue:
        ab_word = queue.popleft()
        if ab_word.start == word_len:
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            result.append(''.join(ab_word.str))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            queue.append(AbbreviatedWord(list(ab_word.str), ab_word.start + 1, ab_word.count + 1))

            # restart abbreviating, append the count and the current character to the st
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            new_word = list(ab_word.str)
            new_word.append(word[ab_word.start])
            queue.append(AbbreviatedWord(new_word, ab_word.start + 1, 0))
    return result


def main():
    print("Generalized abbreviation are: " + str(generate_generalized_abbreviation("internship")))
    print("Generalized abbreviation are: " + str(generate_generalized_abbreviation("code")))


main()
