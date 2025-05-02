class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return nums[(n//2)]
        # max_count = count = 1
        # majority = n/2
        # nums.sort()
        # majority_element = nums[0]

        # for i in range(1, n):
        #     if nums[i-1] == nums[i]:
        #         count +=1
        #     if nums[i] != nums[i-1] or i == n - 1:
        #         max_count = max(max_count, count)
        #         if max_count == count and count >= majority:
        #             majority_element = nums[i-1]
        #         else:
        #             count = 0

        # return majority_element
        