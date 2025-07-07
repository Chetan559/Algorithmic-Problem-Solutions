class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stk = []
        map = {')': '(', '}': '{', ']':'['}
        

        for char in s:
            if len(stk) == 0 and char in map:
                return False
            if char == '{' or char == '[' or char == '(':
                stk.append(char)
            elif char in map:
                if len(stk) != 0:
                    temp = stk.pop()
                    if temp != map[char]:
                        return False
                
        if len(stk) == 0:
            return True
        return False