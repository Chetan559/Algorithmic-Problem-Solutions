class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Map_s_2_t = {}
        Map_t_2_s = {}

        for key in zip(s, t):
            # print(key)
            # print(key[1])
            if key[0] in Map_s_2_t:
               if Map_s_2_t[key[0]] != key[1]:
                    return False
            else:
                Map_s_2_t[key[0]] = key[1] 
            
            if key[1] in Map_t_2_s:
               if Map_t_2_s[key[1]] != key[0]:
                    return False 
            else:
                Map_t_2_s[key[1]] = key[0] 

        return True
