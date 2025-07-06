class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        map_s = Counter(s)
        map_t = Counter(t)
        
        for key in map_s:
            if map_s[key] != map_t[key]:
                return False


        return True