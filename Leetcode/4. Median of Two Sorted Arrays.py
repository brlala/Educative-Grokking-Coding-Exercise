class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
        O(log(min(m,n))
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            # ensuring that the first list is alwys shorter
            nums1, nums2 = nums2, nums1
            m, n = n, m
        i_min, i_max = 0, m
        half_len = (m + n + 1) // 2

        while i_min <= i_max:
            # partition into 2 equal parts
            i = (i_min + i_max) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must move partition to right
                i_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must move partition to left
                i_max = i - 1
            else:
                # i is at correct spot
                if i == 0:  # edge case where one of the array is empty
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                # need to find average for median
                if i == m:  # edge case where one of the array is empty
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums2[j], nums1[i])

                return (min_of_right + max_of_left) / 2