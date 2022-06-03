class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.dp=matrix.copy()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                self.dp[i][j]+=self.dp[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1==0:
            sumi=0
            for i in range(row1,row2+1):
                sumi+=self.dp[i][col2]
            return sumi
        else:
            sumi=0
            for i in range(row1,row2+1):
                sumi+=(self.dp[i][col2]-self.dp[i][col1-1])
            return sumi


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)