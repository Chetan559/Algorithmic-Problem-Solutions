class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        prt1 = nums[0]
        prt2 = slow

        while prt1 != prt2:
            prt1 = nums[prt1]
            prt2 = nums[prt2]
        
        return prt1
        
        # print(nums)
        # nums.sort()
        # print(nums)
        # for i in range(1, len(nums)):
            # if nums[i-1] == nums[i]:
                # return nums[i]