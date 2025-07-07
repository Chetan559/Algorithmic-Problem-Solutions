class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        hash_map = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            # '/': operator.truediv
            '/': lambda a, b: int(a/b)
            }

        stk = []
        res = 0

        for i in range(len(tokens)):
            if tokens[i] not in hash_map:
                stk.append(int(tokens[i]))
            else:
                val1, val2 = stk.pop(), stk.pop()
                res = hash_map[tokens[i]](val2, val1)
                stk.append(res)
            
        return stk.pop()