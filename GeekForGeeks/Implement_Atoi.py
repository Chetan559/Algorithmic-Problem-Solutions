#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        sign = 1
        result = 0
        zero = 1
        s = s.strip()
        
        for i in range(len(s)):
            if s[i] == "-":
                sign = -1
            if s[i] != '0':
                zero = 0
            if s[i].isalpha():
                return result*sign
            if zero == 0 and s[i] <= '9' and s[i] >= '0':
                result = result*10 + (ord(s[i]) - ord('0'))
        
        return result*sign 
