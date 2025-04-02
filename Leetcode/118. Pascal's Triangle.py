class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        if numRows >= 1:
            output.append([1])
            # print(output)
        if numRows >= 2:
            output.append([1,1])
            # print(output)

        for i in range(2, numRows):
            row = [1]*(i+1)  
            for j in range(1, i):
                row[j]= output[i-1][j-1] + output[i-1][j]
            output.append(row)
            # print(output)

        return output        