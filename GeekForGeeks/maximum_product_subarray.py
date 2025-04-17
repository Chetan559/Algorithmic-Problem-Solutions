#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		
        max_product = current_max_product = current_min_product = arr[0]
        
        for i in range(1, len(arr)):
            prev_min, prev_max = current_min_product, current_max_product
            current_min_product = min(arr[i], prev_max*arr[i], prev_min*arr[i])
            current_max_product = max(arr[i], prev_max*arr[i], prev_min*arr[i])
            max_product = max(max_product, current_max_product, current_min_product)
            
        return max_product

