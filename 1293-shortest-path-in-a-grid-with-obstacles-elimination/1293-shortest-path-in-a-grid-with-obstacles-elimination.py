from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        
        q=deque()
        if grid[0][0]==1:
            k-=1
            
        q.append((0,0,0))
        dp=[[[0]*m for i in range(n)]for _ in range(k+1)]
        dp[0][0][0]=1
        diri =[[-1,0],[1,0],[0,1],[0,-1]]
        res=0
        while q:
            leng=len(q)
            for _ in range(leng):
                ro,co,curk=q.popleft()
                if ro==n-1 and co==m-1:
                    return res
                for u,v in diri:
                    i=ro+u
                    j=co+v
                    nex=curk
                    if i>-1 and j>-1 and i<n and j<m:
                        if grid[i][j]==1:
                            nex+=1
                        if nex<=k and dp[nex][i][j]==0:
                            dp[nex][i][j]=1
                            q.append((i,j,nex))
            res+=1                
        return -1     
        
        