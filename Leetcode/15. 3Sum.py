class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k:
                        if nums[j] == nums[j-1]:
                            j += 1 
                        else:
                            break
                    
                    while j < k:
                        if nums[k] == nums[k+1]:
                            k -= 1
                        else:
                            break

                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
    
        return res