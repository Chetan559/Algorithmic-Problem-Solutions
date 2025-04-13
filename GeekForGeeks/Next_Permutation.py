#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        min = -1
        for i in range(n-2,-1,-1):
            if  arr[i] < arr[i + 1]:
                min = i
                break
            
        if min == -1:
            return arr.reverse()
        
        for i in range(n-1, min,-1):
            if arr[i] > arr[min]:
                arr[min], arr[i] = arr[i], arr[min]
                break
        
        arr[min + 1:] = reversed(arr[min + 1:])
        
        return arr