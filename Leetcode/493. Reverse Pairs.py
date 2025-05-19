class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        j =  n - 1
        res = 0
        
        for i in range(n - 1):
            if nums[i] > 2*nums[j]:
                res += 1
        
        return res