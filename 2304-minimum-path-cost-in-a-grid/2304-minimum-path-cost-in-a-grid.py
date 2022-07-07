import math
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[math.inf]*n for i in range(m)]
        for i in range(n):
            dp[0][i]=grid[0][i]
        for i in range(1,m):
            for j in range(n):
                ans=math.inf
                for k in range(n):
                    ans=min(ans,moveCost[grid[i-1][k]][j]+dp[i-1][k])
                dp[i][j]=ans+grid[i][j]
        return min(dp[-1])        