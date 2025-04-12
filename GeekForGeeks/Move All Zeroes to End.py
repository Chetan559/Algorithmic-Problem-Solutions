#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
        size = len(arr)
        count = 0
        
        for i in range(size):
            if arr[i] != 0:
                arr[count],arr[i] = arr[i],arr[count]
                count += 1
                
        
        return arr 
