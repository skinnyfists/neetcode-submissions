class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = (right + left) // 2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] > target:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return -1