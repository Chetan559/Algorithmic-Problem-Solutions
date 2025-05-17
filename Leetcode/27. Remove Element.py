class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums) - 1):
            if nums[i] == val:
                n += 1
                for j in range(i, len(nums) - 1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            
        return n

        