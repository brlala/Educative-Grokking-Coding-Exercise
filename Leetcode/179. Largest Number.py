class Comparable:
    def __init__(self, n):
        self.value = str(n)

    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_nums = [Comparable(n) for n in nums]
        new_nums.sort()
        value = ''.join(n.value for n in new_nums)
        return value.lstrip('0') or '0'

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        # # 1 if a+b>b+a else -1 if a+b<b+a else 0
        compare = lambda a, b: -1 if a + b > b + a else 0
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))