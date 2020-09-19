# Problem Statement
# Given a string and a list of words, find all the starting indices of substrings in the given string that are a
# concatenation of all the given words exactly once without any overlapping of words. It is given that all words
# are of the same length.
from collections import defaultdict, Counter


def find_substring_from_words(string, words):
    """
    Time: O(n*m*len)
    Space: O(N+M)
    """
    wCounter = Counter(words)
    word_count = len(words)
    word_length = len(words[0])
    results = []

    # Loop over word length
    for i in range(word_length):
        left = i
        words_seen = defaultdict(int)
        count = 0
        # Loop over the string
        for j in range(i, len(string) - word_length + 1, word_length):
            # Get a word from observed substring
            word = string[j:j + word_length]
            # check if it is a valid word
            if word in wCounter:
                words_seen[word] += 1
                count += 1
                # Shift the window as long as we have encountered more number of a word than is needed
                # Note that we can shift the window by word length directly as the outer loop is there to
                # make sure that anything is not missed out
                # This solution will give indices out of order by OJ accepts it.
                while words_seen[word] > wCounter[word]:
                    words_seen[string[left:left + word_length]] -= 1
                    left += word_length
                    count -= 1
                # Count will be equal to word_count only when we all the words are read the exact number of times needed
                if count == word_count:
                    results.append(left)
            # If is not a valid word then just skip over the current word (Don't worry about the middle characters
            # outer loop will take care of it)
            else:
                left = j + word_length
                words_seen = defaultdict(int)
                count = 0
    return results


def find_substring_from_words(string, words):
    """
    Time: O(n*m*len)
    Space: O(N+M)
    """
    wCounter = Counter(words)
    word_count = len(words)
    word_length = len(words[0])
    results = []

    for i in range(word_length):
        left = i
        words_seen = defaultdict(int)
        count = 0
        for j in range(i, len(string)-word_length+1, word_length):
            word = string[j:j+word_length]
            if word in wCounter:
                words_seen[word] += 1
                count += 1

                while words_seen[word] > wCounter[word]:
                    words_seen[string[left:left+word_length]] -= 1
                    left += word_length
                    count -= 1
                if count == word_count:
                    results.append(left)
            # If is not a valid word then just skip over the current word (Don't worry about the middle characters
            # outer loop will take care of it)
            else:
                left = j + word_length
                words_seen = defaultdict(int)
                count = 0
    return results


# print(find_substring_from_words('catfoxcat', ["cat", "fox", "cat"]) == [0])
print(find_substring_from_words('catfoxcat', ["cat", "fox"]) == [0, 3])
# print(find_substring_from_words('catcatfoxfox', ["cat", "fox"]) == [3])
