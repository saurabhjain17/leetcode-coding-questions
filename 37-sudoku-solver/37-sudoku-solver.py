class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        global ans
        ans=-1
        def checksquare( row, col, ch):
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == ch:
                        return False
            return True
        def checkrow( row, ch):
            for col in range(9):
                if board[row][col] == ch:
                    return False
            return True

        def checkcol( col, ch):
            for row in range(9):
                if board[row][col] == ch:
                    return False
            return True
        def isvalid( row, col, ch):
            boxrow = row - row%3
            boxcol = col - col%3
            if checkrow(row,ch) and checkcol(col,ch) and checksquare(boxrow, boxcol, ch):
                return True
            return False
        def findUnassigned():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        return row, col
            return -1, -1
        def solve():
            
            row, col = findUnassigned()
        #no unassigned position is found, puzzle solved
            if row == -1 and col == -1:
                return True
            for num in ["1","2","3","4","5","6","7","8","9"]:
                if isvalid(row, col, num):
                    board[row][col] = num
                    if solve():
                        return True
                    board[row][col] = "."
            return False     
        return solve()
        # return ans