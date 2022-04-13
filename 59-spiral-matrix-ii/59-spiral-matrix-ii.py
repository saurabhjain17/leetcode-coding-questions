class Solution:
    def solve(self,mat,val,start,end):
        if end==start:
            return
        if end-start==1:
            mat[start][start]=val
            return
        for i in range(start,end):
            mat[start][i]=val
            val+=1
        for i in range(start+1,end):
            mat[i][end-1]=val
            val+=1
        for i in range(end-2,start-1,-1):
            mat[end-1][i]=val
            val+=1
        for i in range(end-2,start,-1):
            mat[i][start]=val
            val+=1
        print(mat)    
        self.solve(mat,val,start+1,end-1)    
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for _ in range(n)]
        self.solve(mat,1,0,n)
        return mat