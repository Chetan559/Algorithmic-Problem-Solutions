class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        i = 0
        for j in range(len(t)):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
            else:
                continue
        
        if i == len(s):
            return True
        else:
            return False