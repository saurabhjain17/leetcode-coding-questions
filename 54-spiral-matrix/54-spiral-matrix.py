class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ro=len(matrix)
        co=len(matrix[0])
        top=left=0
        right=co-1
        bottom=ro-1
        ans=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            if top==bottom:
                break
            for i in range(top+1,bottom+1):
                ans.append(matrix[i][right])
            if left==right:
                break
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom][i])
            for i in range(bottom-1,top,-1):
                ans.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
        return ans    
            