class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        res = False
        left, right, up, down = 0, n-1, 0, m-1
        row = -1

        while up <= down:
            mid = (up + down)//2
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][n-1]:
                up = mid + 1
            else:
                row = mid
                break     

        # for i in range(m):
        #     if target < matrix[i][0] and i > 0:
        #         row = i - 1
        #         break

        # if target < matrix[m-1][n-1] and target >= matrix[m-1][0]:
        #     row = m - 1

        print(row)
        if row != -1 and target <= matrix[row][n-1]:
            while left <= right:
                mid = (left + right)//2

                if target > matrix[row][mid]:
                    left = mid + 1
                elif target < matrix[row][mid]:
                    right = mid - 1
                elif target == matrix[row][mid]:
                    res = True
                    break    
        else:
            return res 

        return res