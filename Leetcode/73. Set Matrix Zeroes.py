class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        print(rows, cols)
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for j in range(cols):
                        if matrix[row][j] != 0:
                            matrix[row][j] = 'a'
                    for i in range(rows):
                        if matrix[i][col] != 0:
                            matrix[i][col] = 'a'
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 'a':
                    matrix[row][col] = 0


# better solution

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        colz = [1] * cols
        rowz = [1] * rows
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowz[row] =0
                    colz[col] = 0

        for row in range(rows):
            for col in range(cols):
                if (rowz[row] == 0 or colz[col] == 0):
                    matrix[row][col] = 0

                

