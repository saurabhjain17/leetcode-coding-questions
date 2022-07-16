class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0]==")" or grid[-1][-1]=="(":
            return False
        rows=len(grid)
        cols=len(grid[0])
        dp=dict()
        score={"(":1,")":-1}
        def rec(ro,co,scor):
            if scor<0:
                return False
            if ro==rows-1 and co==cols-1:
                scor+=score[grid[ro][co]]
                return scor==0
            if (ro,co,scor) not in dp:
                total=False
                if ro+1<rows:
                    
                    total=total or rec(ro+1,co,scor+score[grid[ro][co]])
                if co+1<cols:
                    total=total or rec(ro,co+1,scor+score[grid[ro][co]]) 
                dp[(ro,co,scor)]=total
            return dp[(ro,co,scor)]
        return rec(0,0,0)