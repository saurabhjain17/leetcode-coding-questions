class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        new_grid=[0]*(m*n)
        total=m*n
        p=0
        for i in range(m):
            for j in range(n):
                new_grid[p]=grid[i][j]
                p+=1
        k%=total
        new=total-k
        new_grid=new_grid[:new][::-1]+new_grid[new:][::-1]
        new_grid=new_grid[::-1]
        p=0
        for i in range(m):
            for j in range(n):
                grid[i][j]=new_grid[p]
                p+=1
        return grid        
                
      