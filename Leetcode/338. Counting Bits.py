class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            current = i
            one_bits = 0
            while current:
                if current & 1:
                    one_bits += 1
                current >>= 1
            res.append(one_bits)
        return res

    def countBits(self, num: int) -> List[int]:
        """
        Dynamic programming, # of bits is num/2, +1 if it's odd
        https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation
        Base 2: 111    Base 10: 7
        """
        res = [0]
        for i in range(1, num + 1):
            res += [res[i >> 1] + i % 2]
        return res
