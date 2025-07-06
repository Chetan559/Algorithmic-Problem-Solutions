class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                if abs(hashMap[nums[i]] - i) <= k:
                    return True
                else:
                    hashMap[nums[i]] = i
            else:
                hashMap[nums[i]] = i

        return False