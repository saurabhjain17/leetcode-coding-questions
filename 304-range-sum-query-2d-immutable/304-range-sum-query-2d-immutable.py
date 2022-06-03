class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.dp=matrix.copy()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                self.dp[i][j]+=self.dp[i][j-1]
        for j in range(n):
            for i in range(1,m):
                self.dp[i][j]+=self.dp[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1==0 and row1==0:
            return self.dp[row2][col2]
        elif row1==0:
            return self.dp[row2][col2]-self.dp[row2][col1-1]
        elif col1==0:  
            return self.dp[row2][col2]-self.dp[row1-1][col2]
        else:
            return self.dp[row2][col2]-self.dp[row1-1][col2]-self.dp[row2][col1-1]+self.dp[row1-1][col1-1]
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)