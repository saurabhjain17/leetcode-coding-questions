import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=queue.Queue()
        time=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.put((i,j))
        while q.empty() is False:
            flag=0
            length=q.qsize()
            for i in range(length):
                ro,co=q.get()
                if ro+1<row and grid[ro+1][co]==1:
                    q.put((ro+1,co))
                    grid[ro+1][co]=2
                    flag=1
                if co+1<col and grid[ro][co+1]==1:
                    q.put((ro,co+1))
                    grid[ro][co+1]=2
                    flag=1
                if ro-1>-1 and grid[ro-1][co]==1:
                    q.put((ro-1,co))
                    grid[ro-1][co]=2
                    flag=1
                if co-1>-1 and grid[ro][co-1]==1:
                    q.put((ro,co-1))
                    grid[ro][co-1]=2
                    flag=1    
            if flag==1:
                time+=1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1
        return time          