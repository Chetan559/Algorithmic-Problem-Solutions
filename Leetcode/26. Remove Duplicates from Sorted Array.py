class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m, n = 0 , 1

        while n < len(nums):
            if nums[n] != nums[m]:
                nums[m + 1] = nums[n]
                m += 1
            else:
                n += 1

        return m + 1
                