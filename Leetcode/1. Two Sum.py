class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  brute force
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        #  hashmap
        hashMap = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashMap:
                return [i, hashMap[target - nums[i]]]
            else:
                hashMap[nums[i]] = i