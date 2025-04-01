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
