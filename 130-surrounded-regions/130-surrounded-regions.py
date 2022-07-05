class Solution:
    def fs(self,vis,ro,co,board,n,m):
        vis[ro][co]=1
        
        queue=[[ro,co]]
        while queue:
            ro,co=queue.pop(0)
            for ind in [[1,0],[0,1],[-1,0],[0,-1]]:
                r=ro+ind[0]
                c=co+ind[1]
                if r<n and r>-1 and c<m and c>-1 and board[r][c]=="O" and vis[r][c]==0:
                    queue.append([r,c])
                    vis[r][c]=1
                   
    def dfs(self,vis,ro,co,board,n,m):
        vis[ro][co]=1
        board[ro][co]="X"
        queue=[[ro,co]]
        while queue:
            ro,co=queue.pop(0)
            for ind in [[1,0],[0,1],[-1,0],[0,-1]]:
                r=ro+ind[0]
                c=co+ind[1]
                if r<n and r>-1 and c<m and c>-1 and board[r][c]=="O" and vis[r][c]==0:
                    queue.append([r,c])
                    vis[r][c]=1
                    board[r][c]="X"
                    
                
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        vis=[[0]*m for i in range(n)]
        for i in range(m):
            if board[0][i]=="O" and vis[0][i]==0:
                self.fs(vis,0,i,board,n,m)
            if board[n-1][i]=="O" and vis[n-1][i]==0:
                self.fs(vis,n-1,i,board,n,m) 
        for i in range(n):
            if board[i][0]=="O" and vis[i][0]==0:
                self.fs(vis,i,0,board,n,m)
            if board[i][m-1]=="O" and vis[i][m-1]==0:
                self.fs(vis,i,m-1,board,n,m)
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j]=="O" and vis[i][j]==0:
                    self.dfs(vis,i,j,board,n,m)
        return board            
                