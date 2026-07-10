class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, num_a in enumerate(nums):
            # can't satisfy condition if all numbers are positive
            if num_a > 0:
                break

            if i > 0 and nums[i - 1] == num_a:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                current = num_a + nums[left] + nums[right]
                if current == 0:
                    triplets.append([nums[left], nums[right], num_a])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return triplets