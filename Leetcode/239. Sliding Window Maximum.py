class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return
        n = len(nums)
        mono_queue = deque()
        res = []
        for idx, num in enumerate(nums):
            # make sure the rightmost one is the smallest
            while mono_queue and nums[mono_queue[-1]] < nums[idx]:
                mono_queue.pop()
            mono_queue.append(idx)

            # make sure the leftmost one is in-bound
            if idx - mono_queue[0] >= k:
                mono_queue.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if idx + 1 >= k:
                res.append(nums[mono_queue[0]])
        return res
