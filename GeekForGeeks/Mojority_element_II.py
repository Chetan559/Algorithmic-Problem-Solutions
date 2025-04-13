class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        arr.sort()
        majority = n / 3
        prev = 0
        
        candidate = []
        
        vote = 1
        for i  in range(1, n):
            if arr[i] == arr[i-1]:
                vote += 1
            else:
                if vote > majority:
                    candidate.append(arr[i - 1])
                vote = 1
                
        if vote > majority:
            candidate.append(arr[-1])

        return candidate