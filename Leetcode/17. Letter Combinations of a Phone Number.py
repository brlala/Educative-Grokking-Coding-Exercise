class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_map = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        res = []
        self.helper(digits, [], num_map, res)
        return res

    def helper(self, digits, path, num_map, res):
        if not digits:
            res.append(''.join(path))
            return

        for i in range(len(digits)):
            if i != 0:
                return
            for w in num_map[digits[i]]:
                self.helper(digits[i + 1:], path + [w], num_map, res)

    def letterCombinations(self, digits: str) -> list[str]:
        """
        Backtracking
        :param digits:
        :return:
        """
        num_map = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        res = []
        self.helper(digits, 0, "", num_map, res)
        return res

    def helper(self, digits, index, path, num_map, res):
        if index >= len(digits):
            res.append(path)
            return

        string1 = num_map[digits[index]]
        for s in string1:
            self.helper(digits, index+1, path+s, num_map, res)



a = Solution()
print(a.letterCombinations("23"))
