class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        encountered TLE, complexity n^2
        """
        self.max_area = 0
        for i in range(len(heights)):
            self.max_area = max(self.max_area, self.count_area(i, heights))
        return self.max_area

    def count_area(self, index, heights):
        left = right = index
        while left > 0 and heights[left - 1] >= heights[index]:
            left -= 1
        while right < len(heights) - 1 and heights[right + 1] >= heights[index]:
            right += 1
        return (right - left + 1) * heights[index]

    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        using stack, complexity n
        https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/452612/Thinking-Process-for-Stack-Solution
        """
        stack = [(-1, 0)]
        heights.append(0)
        max_area = 0
        for idx, height in enumerate(heights):
            while height < stack[-1][1]:
                elem_index, h = stack.pop()
                width = idx - stack[-1][0] - 1
                max_area = max(max_area, width * h)
            stack += (idx, height),
        heights.pop()
        return max_area





a = Solution()
print(a.largestRectangleArea([2, 1, 5, 6, 2, 3]))
