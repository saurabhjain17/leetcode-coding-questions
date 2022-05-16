class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        vis=[[0]*n for i in range(n)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q=[(0,0,1)]
        vis[0][0]=1
        while q:
            i,j,dis=q.pop(0)
            if i==n-1 and j==n-1:
                return dis
            if i+1<n and grid[i+1][j]==0 and vis[i+1][j]==0:
                vis[i][j]=1
                q.append((i+1,j,dis+1))
            if j+1<n and grid[i][j+1]==0 and vis[i][j+1]==0:
                vis[i][j+1]=1
                q.append((i,j+1,dis+1))
                
            if i+1<n and j+1<n and grid[i+1][j+1]==0 and vis[i+1][j+1]==0:
                vis[i+1][j+1]=1
                q.append((i+1,j+1,dis+1))
                
            if i-1>-1 and grid[i-1][j]==0 and vis[i-1][j]==0:
                vis[i-1][j]=1
                q.append((i-1,j,dis+1))
                
            if j-1>-1 and grid[i][j-1]==0 and vis[i][j-1]==0:
                vis[i][j-1]=1
                q.append((i,j-1,dis+1))
                
            if i+1<n and j-1>-1 and grid[i+1][j-1]==0 and vis[i+1][j-1]==0:
                vis[i+1][j-1]=1
                q.append((i+1,j-1,dis+1))
                
            if i-1>-1 and j+1<n and grid[i-1][j+1]==0 and vis[i-1][j+1]==0:
                vis[i-1][j+1]=1
                q.append((i-1,j+1,dis+1))
            if i-1>-1 and j-1>-1 and grid[i-1][j-1]==0 and vis[i-1][j-1]==0:
                vis[i-1][j-1]=1
                q.append((i-1,j-1,dis+1)) 
        return -1        
                