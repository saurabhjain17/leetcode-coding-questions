class Solution:
    def rec(self,row,ro):
        left=[-1]*ro
        stack=[]
        n=0
        stack.append((row[0],0))
        n+=1
        for i in range(1,ro):
            if n==0:
                stack.append((row[i],i))
                n+=1
            else:
                while n>0 and stack[-1][0]>=row[i]:
                    stack.pop(-1)
                    n-=1
                if n!=0:
                    left[i]=stack[-1][1]
                stack.append((row[i],i))
                n+=1
        right=[ro]*ro
        n=0
        stack=[]
        stack.append((row[ro-1],ro-1))
        n+=1
        for i in range(ro-2,-1,-1):
            if n==0:
                stack.append((row[i],i))
                n+=1
            else:
                while n>0 and stack[-1][0]>=row[i]:
                    stack.pop(-1)
                    n-=1
                if n!=0:
                    right[i]=stack[-1][1]
                stack.append((row[i],i))
                n+=1
        maxi=0
        for i in range(ro):
            
                maxi=max(maxi,(right[i]-left[i]-1)*row[i])
        return maxi        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ro=len(matrix)
        co=len(matrix[0])
        for i in range(ro):
            for j in range(co):
                matrix[i][j]=int(matrix[i][j])
                if i==0:
                    continue
                if matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]
        maxi=0            
        for perRow in matrix:
            maxi=max(maxi,self.rec(perRow,co))
        return maxi   