class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lefts = [None]*n
        rights = [None]*n
        lefts[0] = rights[n - 1] = 1

        for i in range(1, n):
            lefts[i] = lefts[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            rights[i] = rights[i + 1] * nums[i + 1]

        for i in range(n):
            nums[i] = lefts[i] * rights[i]
        
        return nums