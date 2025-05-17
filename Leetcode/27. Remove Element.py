class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        m, n = 0, len(nums) - 1
        while n >= m:
            if nums[m] == val:
                k += 1
                nums[n], nums[m] = nums[m], nums[n]
                n -= 1
            else:
                m += 1

        return (len(nums) - k)

        