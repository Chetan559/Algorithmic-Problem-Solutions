Second Largest
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max = -1
        s_max = -1
        for _ in range(len(arr)):
            if arr[_] > max:
                max = arr[_]
        
        
        for _ in range(len(arr)):
            if arr[_] > s_max and arr[_] < max:
                s_max = arr[_]
        
        return s_max