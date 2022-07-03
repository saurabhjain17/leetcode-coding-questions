class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for i in range(n)]
        vis=[[0]*m for i in range(n)]
        def rec(dp,grid,vis,n,m,i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            vis[i][j]=1
            if dp[i][j]==-1:
                counti=1
                if i+1<n and grid[i+1][j]>grid[i][j]:
                    counti+= rec(dp,grid,vis,n,m,i+1,j)
                if j+1<m and grid[i][j+1]>grid[i][j]:
                    counti+=rec(dp,grid,vis,n,m,i,j+1)
                if i-1>-1 and grid[i-1][j]>grid[i][j]:
                    counti+=rec(dp,grid,vis,n,m,i-1,j)
                if j-1>-1 and grid[i][j-1]>grid[i][j]:
                    counti+= rec(dp,grid,vis,n,m,i,j-1)
                dp[i][j]=counti
            return dp[i][j]    
        
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0:
                    rec(dp,grid,vis,n,m,i,j)
                  
                    
        sumi=0
        for i in range(n):
            for j in range(m):
                
                sumi+=dp[i][j]
        return sumi %(1000000007)       