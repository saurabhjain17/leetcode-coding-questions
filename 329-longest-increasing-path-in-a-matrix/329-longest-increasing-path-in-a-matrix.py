class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        mat=[[1]*m for _ in range(n)]
        def dfs(i,j,matrix,mat,n,m):
            q=[(i,j,mat[i][j])]
            while q:
                s,t,val=q.pop(-1)
                if s+1<n and matrix[s+1][t]>matrix[s][t] and mat[s+1][t]<mat[s][t]+1:
                    mat[s+1][t]=mat[s][t]+1
                    q.append((s+1,t,mat[s+1][t]))
                if t+1<m and matrix[s][t+1]>matrix[s][t] and mat[s][t+1]<mat[s][t]+1:
                    mat[s][t+1]=mat[s][t]+1
                    q.append((s,t+1,mat[s][t+1]))
                if s-1>-1 and matrix[s-1][t]>matrix[s][t] and mat[s-1][t]<mat[s][t]+1:
                    mat[s-1][t]=mat[s][t]+1
                    q.append((s-1,t,mat[s-1][t]))
                if t-1>-1 and matrix[s][t-1]>matrix[s][t] and mat[s][t-1]<mat[s][t]+1:
                    mat[s][t-1]=mat[s][t]+1
                    q.append((s,t-1,mat[s][t-1]))    
        for i in range(n):
            for j in range(m):
                dfs(i,j,matrix,mat,n,m)
        maxi=max(mat[0])
        for i in range(n):
            maxi=max(maxi,max(mat[i]))
        return maxi    