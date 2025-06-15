class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        if nums[0] == 0:
            return False

        k = nums[0]
        i = 1
        while k>0 and i < n:
            k -= 1
            if nums[i] > k:
                k = nums[i]
            if k == 0 and i != n - 1:
                return False
            i += 1
        
        return True