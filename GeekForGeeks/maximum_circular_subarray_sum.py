#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    
    max_sum = current_sum = min_sum = current_min = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        current_min = min(arr[i], current_min + arr[i])
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_min)
        
    total = sum(arr)
    circular_max = total - min_sum
    
    return max(circular_max, max_sum)
    