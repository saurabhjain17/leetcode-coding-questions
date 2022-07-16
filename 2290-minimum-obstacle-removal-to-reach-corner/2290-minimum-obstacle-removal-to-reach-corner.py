import heapq
import math
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap=[]
        n=len(grid)
        m=len(grid[0])
        dp=[[math.inf]*m for i in range(n)]
        dp[0][0]=grid[0][0]
        heapq.heappush(heap,(grid[0][0],0,0))
        while heap:
            dis,ro,co=heapq.heappop(heap)
            if ro+1<n and dp[ro+1][co]>dis+grid[ro+1][co]:
                dp[ro+1][co]=dis+grid[ro+1][co]
                heapq.heappush(heap,(dp[ro+1][co],ro+1,co))
                
            if co+1<m and dp[ro][co+1]>dis+grid[ro][co+1]:
                dp[ro][co+1]=dis+grid[ro][co+1]
                heapq.heappush(heap,(dp[ro][co+1],ro,co+1))
            if ro-1>-1 and dp[ro-1][co]>dis+grid[ro-1][co]:
                dp[ro-1][co]=dis+grid[ro-1][co]
                heapq.heappush(heap,(dp[ro-1][co],ro-1,co))
            if co-1>-1 and dp[ro][co-1]>dis+grid[ro][co-1]:
                dp[ro][co-1]=dis+grid[ro][co-1]
                heapq.heappush(heap,(dp[ro][co-1],ro,co-1))   
        return dp[-1][-1]        