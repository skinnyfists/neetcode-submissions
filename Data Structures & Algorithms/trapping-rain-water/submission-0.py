class Solution:
    def trap(self, heights: List[int]) -> int:
        water = 0
        left_bars = [0] * len(heights)
        right_bars = [0] * len(heights)
        for i in range(len(heights)):
            j = len(heights) - 1 - i
            if i > 0:
                left_bars[i] = max(left_bars[i - 1], heights[i])
            else:
                left_bars[i] = heights[i]
            if j < len(heights) - 1:
                right_bars[j] = max(right_bars[j + 1], heights[j])
            else:
                right_bars[j] = heights[j]
        return sum(min(left_bars[i], right_bars[i]) - height for i, height in enumerate(heights))
        