class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp=dict()
        modu=10**9+7
        def dfs(ro,co,mov):
            if ro>=m or ro<0 or co>=n or co<0:
                return 1
            if mov==0:
                return 0
            if (ro,co,mov) not in dp:
                total=0
                for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ne_ro=ro+i
                    ne_co=co+j
                    total+=dfs(ne_ro,ne_co,mov-1)
                    
                dp[(ro,co,mov)]=total%modu
            return dp[(ro,co,mov)]    
        return dfs(startRow,startColumn,maxMove)