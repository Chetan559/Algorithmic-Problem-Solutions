class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n/3
        curr_count = 1
        res =[]
        nums.sort()
        for i in range(n-1):
            if nums[i + 1] == nums[i]:
                curr_count += 1
            else:
                if curr_count > majority:
                    res.append(nums[i])
                curr_count = 1 

        if curr_count > majority:
            res.append(nums[-1])
           
        return res
        