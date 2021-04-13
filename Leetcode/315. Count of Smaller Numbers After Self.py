# modified binary sort to count smaller after self
class Solution:
    def countSmaller(self, nums):
        def sort(enums):  # index, value
            half = len(enums)//2
            if half:
                left, right = sort(enums[:half]), sort(enums[half:])
                # start sorting from bigger to lower
                for i in range(len(enums))[::-1]:
                    # if left last is bigger than right last, add all right to result and put it to correct place
                    # also need to consider about left empty and righ empty
                    if not right or (left and left[-1][1] > right[-1][1]):
                        smaller[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    # if left last is smaller than right, just put right to correct place
                    else:
                        enums[i] = right.pop()
            return enums
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


a = Solution()
print(a.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0])
