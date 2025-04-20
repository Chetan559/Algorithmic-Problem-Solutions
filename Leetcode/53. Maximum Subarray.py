class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sum_so_far = nums[0]

        for i in range(1, len(nums)):
            sum_so_far = max(nums[i], sum_so_far + nums[i])
            max_sum = max(max_sum, sum_so_far)

        return max_sum
        