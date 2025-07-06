class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        Map_patter_2_s = {}
        Map_s_2_patter = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for key in zip(pattern, s):
            # if key[0] and (not key[1]):
            #     return False
            # if key[1] and (not key[0]):
            #     return False

            if key[0] in Map_patter_2_s:
                if Map_patter_2_s[key[0]] != key[1]:
                    return False
            else:
                Map_patter_2_s[key[0]] = key[1]

            if key[1] in Map_s_2_patter:
                if Map_s_2_patter[key[1]] != key[0]:
                    return False
            else:
                Map_s_2_patter[key[1]] = key[0]

        return True