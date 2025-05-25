class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start_index = 0
        curr_count = 0
        for i in range(len(s)):    
            if s[i] not in s[start_index : i]:
                curr_count += 1
            else:
                start_index = s[start_index:].find(s[i]) + start_index + 1
                res = max(res, curr_count)
                curr_count = i - start_index + 1

        res = max(res, curr_count)
        
        return res