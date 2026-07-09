class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        biggest = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            biggest = max(biggest, current)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return biggest