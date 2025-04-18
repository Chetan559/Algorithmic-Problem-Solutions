#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        sign = 1
        result = 0
        n = len(s)
        nums = 0
        index = 0
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
        
        if s[i] == '-':
            sign = -1
            i+=1
            
        while i < n and '9'>=s[i]>='0':
            result = result*10 + (ord(s[i]) - ord('0'))
            if result*sign > (2**31 - 1):
                return 2**31 - 1
            elif result*sign < (-2**31):
                return -2**31
            i+=1
            
        return result*sign
        # sign = 1
        # result = 0
        # # zero = 1
        # nums = 0
        # index = 0
        # s = s.strip()
        
        # for i in range(len(s)):
        #     if s[i] == "-":
        #         sign = -1
        #     if s[i] != '0':
        #         zero = 0
        #     if result*sign > (2**31 - 1) or result*sign < (-2**31):
        #         if result*sign < (-2**31):
        #             return -2**31
        #         else:
        #             return 2**31 - 1
        #     if s[i].isalpha():
        #         return result*sign
        #     if zero == 0 and s[i] <= '9' and s[i] >= '0':
        #         result = result*10 + (ord(s[i]) - ord('0'))
        
        # return result*sign 
