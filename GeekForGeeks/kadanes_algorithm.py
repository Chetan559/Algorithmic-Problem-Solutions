class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_sum = -100000000
        # fst_index = 0
        # lst_index = 0
        sum_so_far = 0
        # for i in range(len(arr)):
        #     for j in range(i , len(arr)):
        #         sum_so_far += arr[j]
        #         max_sum = max(sum_so_far, max_sum)
        #     sum_so_far = 0    
        
        for i in range(len(arr)):
            sum_so_far = max(arr[i], sum_so_far + arr[i])
            max_sum = max(max_sum, sum_so_far)
        
        return max_sum
