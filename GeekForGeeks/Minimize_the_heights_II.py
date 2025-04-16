#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        # minimum = min(arr)
        # maximum = max(arr)
        # # mid = maximum/2
        # mid = (maximum - minimum)/ 2
        # # print(minimum, maximum, mid)
        
        # for i in range(len(arr)):
        #     if arr[i] >= mid:
        #         arr[i] -= k
        #     else:
        #         arr[i] += k
        
        # # print(arr)
        # minimum = min(arr)
        # maximum = max(arr)
        
        # arr.sort()
        # maximum = arr[-1]
        # minimum = arr[0]
        # mid = (maximum - minimum)/ 2
        
        # for i in range(len(arr)):
        #     if arr[i] > mid and (arr[i] - k) >= minimum:
        #         arr[i] -= k
        #         if arr[i] == min(arr) and arr[i] > minimum:
        #             minimum = arr[i]
        #             mid = (maximum - minimum)/ 2
        #     elif arr[i] <= mid and (arr[i] + k) <= maximum:
        #         arr[i] += k
        #         if arr[i] == max(arr) and arr[i] < maximum:
        #             maximum = arr[i]
        #             mid = (maximum - minimum)/ 2
        
        # print(arr)
        # minimum = min(arr)
        # maximum = max(arr)
        # print(minimum, maximum)
        
        # arr.sort()
        # maximum = arr[-1] - k
        # minimum = arr[0] + k
        # if maximum - minimum > -1:
        #     diffrance = maximum - minimum
    
        # for i in range(len(arr)):
        #     if (arr[i] - k) > minimum:
        #         arr[i] -= k
        #         if max(arr) - min(arr) < diffrance:
        #             diffrance = max(arr) - min(arr)
        #     elif (arr[i] + k) < maximum:
        #         arr[i] += k
        #         if max(arr) - min(arr) < diffrance:
        #             diffrance = max(arr) - min(arr)
        
        # diffrance = max(arr) - min(arr)
        
        # arr.sort()
        # maximum = arr[-1]
        # minimum = arr[0]
        # min_diff = maximum - minimum
        
        
        # for i in range(1, len(arr)):
        #     for j in range(i):
        #         arr[j] += k
        #     for j in range(i, len(arr)):
        #         arr[j] -= k
            
        #     if min(arr) > -1:
        #         minimum = min(minimum, min(arr), arr[0])
        #         maximum = max(maximum, max(arr), arr[-1])
            
        #     if maximum - minimum > -1 and maximum - minimum < min_diff:
        #         min_diff = maximum - minimum
        
        # arr.sort()
        # min_diff = arr[-1] - arr[0]
        
        # for i in range(len(arr)):
        #     if arr[i] < k:
        #         continue
        #     minimum = min(arr[i] + k, arr[0] + k)
        #     maximum = max(arr[i - 1] - k, arr[-1] - k)
        #     min_diff = min(min_diff, maximum - minimum)
        
        
        arr.sort()
        min_diff = arr[-1] - arr[0]
        large = arr[-1] - k
        small = arr[0] + k
        
        for i in range(len(arr) - 1):
            # temp = arr.copy()
            # for j in range(i + 1):
            #     temp[j] += k
            # for j in range(i+1, len(arr)):
            #     temp[j] -= k
            
            maximum = max(large, arr[i] + k)
            minimum = min(small, arr[i+1] - k)
        
            if minimum > -1:
                min_diff = min(min_diff, maximum - minimum)
        
        return min_diff