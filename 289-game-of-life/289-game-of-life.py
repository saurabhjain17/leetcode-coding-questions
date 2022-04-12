class Solution:
    def neighbor(self,board,r,c,m,n):
        if r<0 or c<0 or r>=m or c>=n or board[r][c]==0:
            return 0
        return 1
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        m=len(board)
        n=len(board[0])
        seti=set()
        for r in range(m):
            for c in range(n):
                
                live=self.neighbor(board, r-1, c-1,m,n) + self.neighbor(board, r-1, c,m,n) + self.neighbor(board, r-1, c+1,m,n) +self.neighbor(board, r, c+1,m,n) + self.neighbor(board, r+1, c+1,m,n) + self.neighbor(board, r+1, c,m,n) + self.neighbor(board, r+1, c-1,m,n) +self.neighbor(board, r, c-1,m,n)
                if board[r][c]==1:
                    if live<2 or live>3:
                        seti.add((r,c))
                else:
                    if live==3:
                        seti.add((r,c))
        for s in seti:
            i,j=s
            board[i][j]=(board[i][j]+1)%2
        return board    
                        
        