#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        d = d % len(arr)
        #Your code here
        # for _ in range(d):
        #     # if len(arr) >1:
        #         # arr[0], arr[-1] = arr[-1], arr[0]
        #         for i in range(len(arr) - 1):
        #             arr[i], arr[i+1] = arr[i +1], arr[i]
        n_arr1, n_arr2 = arr[:d], arr[d:]
        n_arr1.reverse()
        n_arr2.reverse()
        f_arr = n_arr1 + n_arr2
        
        for i in range(len(arr)):
            arr[i] = f_arr[len(arr)-1-i]
        
        
        return arr