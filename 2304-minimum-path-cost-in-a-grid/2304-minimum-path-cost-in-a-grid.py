import math
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=grid[0].copy()
        
        for i in range(1,m):
            tem=[0]*n
            for j in range(n):
                ans=math.inf
                for k in range(n):
                    ans=min(ans,moveCost[grid[i-1][k]][j]+dp[k])
                tem[j]=ans+grid[i][j]
            dp=tem    
        return min(dp)        