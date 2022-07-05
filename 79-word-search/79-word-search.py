class Solution:
    def dfs(self,board,word,ro,co,ind,vis,n,r,c):
       
        if ind==n-1:
            if board[r][c]==word[ind]:
                return True
            return False
        if ind==n:
            return True
        
        for tem in [[1,0],[0,1],[-1,0],[0,-1]]:
            left=r+tem[0]
            right=c+tem[1]
            if left>-1 and left<ro and right>-1 and right<co and board[left][right]==word[ind+1] and (left,right) not in vis :
                vis.add((left,right))
                if  self.dfs(board,word,ro,co,ind+1,vis,n,left,right)==True:
                    return True
                vis.discard((left,right))
        return False        
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        ro=len(board)
        co=len(board[0])
        n=len(word)
        for i in range(ro):
            for j in range(co):
                if board[i][j]==word[0]:
                    vis=set()
                    vis.add((i,j))
                    if self.dfs(board,word,ro,co,0,vis,n,i,j)==True:
                        return True
        return False            