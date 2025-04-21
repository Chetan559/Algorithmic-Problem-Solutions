class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums0 = 0
        nums1 = 0
        nums2 = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums0 += 1
            elif nums[i] == 1:
                nums1 += 1
            else:
                nums2 += 1

        # print(nums0, nums1, nums2)
        # nums = nums0 + nums1 + nums2
        # print(nums)

        # a, b, c = len(nums0), len(nums1), len(nums2)

        for i in range(nums0):
            nums[i] = 0
        for i in range(nums0, nums0 + nums1):
            nums[i] = 1
        for i in range(nums0 + nums1, nums0 + nums1 + nums2):
            nums[i] = 2