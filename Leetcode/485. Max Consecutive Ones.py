class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                res = max(res, curr_count)
                curr_count = 0

        res = max(res, curr_count)
        
        return res