#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        initial = arr[0]
        for x in range(len(arr)):
            if arr[x] > 0:
                initial = x
                break
        positive_arr = arr[initial:]

        if positive_arr[0] != 1:
            return 1
        
        small_so_far = small_int = positive_arr[0]
        
        for i in range(1, len(positive_arr)):
            if positive_arr[i-1] + 1 != positive_arr[i] and positive_arr[i-1] != positive_arr[i]:
                if positive_arr[i - 1] + 1 > 0:
                    small_int = positive_arr[i - 1] + 1
                    return small_int
        
        return (positive_arr[-1] + 1)