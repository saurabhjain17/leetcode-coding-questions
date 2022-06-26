class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # n=len(t)
        # m=len(s)
        # dp=[[0]*(m+1) for i in range(n+1)]
        # for i in range(m+1):
        #     dp[0][i]=1
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if t[i-1]==s[j-1]:
        #             dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
        #         else:
        #             dp[i][j]=dp[i][j-1]
        # return dp[-1][-1]  
        
        ###space optimize
        n=len(t)
        m=len(s)
        dp=[1]*(m+1)
        
        for i in range(1,n+1):
            tem=[0]*(m+1)
            for j in range(1,m+1):
                if t[i-1]==s[j-1]:
                    tem[j]=dp[j-1]+tem[j-1]
                else:
                    tem[j]=tem[j-1]
            dp=tem        
        return dp[-1]  