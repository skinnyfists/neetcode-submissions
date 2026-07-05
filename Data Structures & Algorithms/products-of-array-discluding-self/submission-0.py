class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i > 0:
                left[i] = nums[i - 1] * left[i - 1]
            if j < len(nums) - 1:
                right[j] = nums[j + 1] * right[j + 1]
        return [left[i] * right[i] for i in range(len(nums))]