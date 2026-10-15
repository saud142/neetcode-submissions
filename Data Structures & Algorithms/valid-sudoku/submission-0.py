class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #valiadiate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                elif value in seen:
                    return False
                else:
                    seen.add(value)   
            

        #validiate columns
        for j in range(9):
            seen = set()
            for i in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                elif value in seen:
                    return False
                else:
                    seen.add(value)    

    
        #valiadate boxes
        starts =[(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]
        for i,j in starts:
            seen = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    value = board[row][col]
                    if value == ".":
                        continue
                    elif value in seen:
                        return False
                    else:
                        seen.add(value)
        return True                        
