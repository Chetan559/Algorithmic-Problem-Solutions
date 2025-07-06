class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for char in ransomNote:
            if char in hashMap1:
                hashMap1[char] += 1
            else:
                hashMap1[char] = 1

        for char in magazine:
            if char in hashMap2:
                hashMap2[char] += 1
            else:
                hashMap2[char] = 1
        
        for key in hashMap1:
            if hashMap1[key] > hashMap2.get(key, 0):
                return False
 

        return True
