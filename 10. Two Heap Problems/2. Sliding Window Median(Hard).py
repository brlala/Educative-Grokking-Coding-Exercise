from bisect import bisect_left, insort
from typing import List

# https://www.youtube.com/watch?v=4UISvwBwCp0
def median_sliding_window(nums: List[int], k: int) -> List[float]:
    def get_median(nums, k) -> float:
        if k & 1:  # k % 2
            return nums[k // 2]
        else:
            return (nums[k // 2] + nums[k // 2 - 1]) / 2

    output = []
    window = sorted(nums[:k])
    output.append(get_median(window, k))
    for i in range(len(nums) - k):
        window.pop(bisect_left(window, nums[i]))
        insort(window, nums[i + k])
        output.append(get_median(window, k))
    return output


a = [1, -1, 3, 2, 4, 60, 10]
print(median_sliding_window(a, 3))
