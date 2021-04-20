# modified merge sort
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        """
        https://www.youtube.com/watch?v=S6rsAlj_iB4
        Refer to #315 Count of Smaller numbers after self
        """
        def sort(num_list):
            nonlocal res
            half = len(num_list) // 2
            if half:
                left, right = sort(num_list[:half]), sort(num_list[half:])
                pointer_right = 0
                for i in range(len(left)):
                    while pointer_right < len(right) and left[i] > 2 * right[pointer_right]:
                        pointer_right += 1
                    res += pointer_right
            return sorted(num_list)

        res = 0
        sort(nums)
        return res

a = Solution()
print(a.reversePairs([2,4,3,5,1]))