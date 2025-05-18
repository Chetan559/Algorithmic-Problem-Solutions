#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    # Write your code here
    index = max_res = curr_res = 0
    vowel = set('aeiou')
    
    for i in range(k):
        if s[i] in vowel:
            curr_res += 1
    
    max_res = curr_res
    
    for i in range(k, len(s)):
        if s[i-k] in vowel:
            curr_res -= 1
        if s[i] in vowel:
            curr_res += 1
        
        if curr_res > max_res:
            max_res = curr_res
            index = i - k + 1
            
    if max_res == 0:
        return 'Not found!'
    else:
        return s[index: index + k]    
    
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
