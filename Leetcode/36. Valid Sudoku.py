class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        seen = set()

        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
        for j in range(9):
            seen = set()
            for i in range(9):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                seen = set()
                for i in range(3): 
                    for j in range(3): 
                        val = board[x + i][y + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True