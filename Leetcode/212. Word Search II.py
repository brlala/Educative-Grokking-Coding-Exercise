class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1.46am
        if not board or not words: return

        def dfs(i, j, path):
            joined_path = ''.join(path)
            if tree.search(joined_path) and joined_path not in res:
                res.append(joined_path)
            if 0 <= i < m and 0 <= j < n and board[i][j] != '#':
                current_char = board[i][j]  # for marking if visited
                board[i][j] = '#'
                up = dfs(i - 1, j, path + [current_char])
                down = dfs(i + 1, j, path + [current_char])
                left = dfs(i, j - 1, path + [current_char])
                right = dfs(i, j + 1, path + [current_char])
                board[i][j] = current_char
            return

        m = len(board)
        n = len(board[0])
        res = []
        tree = Trie()
        for word in words:
            tree.insert(word)

        for i in range(m):
            for j in range(n):
                dfs(i, j, [])
        return res


a = Solution()
# print(a.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
#             ["oath", "pea", "eat", "rain"]))
# print(a.findWords([["a"]],
# ["a"]))
# print(a.findWords([
#     ["o", "a", "b", "n"],
#     ["o", "t", "a", "e"],
#     ["a", "h", "k", "r"],
#     ["a", "f", "l", "v"]],
#     ["oa", "oaa"]))
# print(a.findWords(
#     [["o", "a", "a", "n"],
#      ["e", "t", "a", "e"],
#      ["i", "h", "k", "r"],
#      ["i", "f", "l", "v"]],
#     ["oath", "pea", "eat", "rain", "oathi", "oathk", "oathf", "oate", "oathii", "oathfi", "oathfii"]))
print(a.findWords(

    [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))


# Correct implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for w in word:
            root = root.children.setdefault(w, TrieNode())
        root.end_node = 1


class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
        tmp = board[i][j]
        if tmp not in node.children: return

        board[i][j] = "#"
        for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, node.children[tmp], i + x, j + y, path + tmp, res)
        board[i][j] = tmp
