class Solution:
    def simplifyPath(self, path: str) -> str:
        # path = path.split('/')
        stk= [] 
        i = 0
        n = len(path)
        while i < n:
            if path[i] == '/':
                i += 1
                continue
            
            temp = ''
            
            while i < n and path[i] != '/':
                temp += path[i]
                i += 1
            if temp != '.':
                stk.append(temp)

            if temp == "..":
                if len(stk) != 0:
                    stk.pop()
                if len(stk) != 0:
                    stk.pop()

            i += 1

        res = ""
        if(len(stk) == 0):
            res = "/"
        while(len(stk) != 0):
            res = "/" + stk.pop() + res


        return res