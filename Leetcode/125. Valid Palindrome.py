class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j:
            while not s[i].isalnum() and i < len(s) -1:
                i += 1
            while not s[j].isalnum() and j > -1:
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True