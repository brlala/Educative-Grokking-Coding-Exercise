class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            width = right - left
            water = max(water, width * min(height[left], height[right]))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return water