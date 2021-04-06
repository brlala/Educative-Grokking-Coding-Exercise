class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Recursive
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        temp = []
        count = 1
        for index in range(1, len(s)):
            if s[index - 1] == s[index]:
                count += 1
            else:
                temp.append(str(count))
                temp.append(s[index - 1])
                count = 1
        temp.append(str(count))
        temp.append(s[-1])
        s = ''.join(temp)
        return s

    def countAndSay(self, n: int) -> str:
        """
        Iterative
        """
        s = '1'
        for _ in range(n - 1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index - 1] == s[index]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index - 1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s

a = Solution()
a.countAndSay(19)