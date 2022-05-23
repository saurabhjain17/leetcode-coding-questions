import math
class Solution:
    def rec(self,strs,m,n,l,dp):
        if m<0 or n<0:
            return -math.inf
        if  l==0:
            return 0
        if (l,m,n) in dp:
            return dp[(l,m,n)]
        
        one=strs[l-1].count("1")
        zero=strs[l-1].count("0")
       
        dp[(l,m,n)]= max(1+self.rec(strs,m-zero,n-one,l-1,dp),self.rec(strs,m,n,l-1,dp))
        return dp[(l,m,n)]
        
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        dp=dict()
        return max(self.rec(strs,m,n,l,dp),0)
        # dp=[[[0]*(m+1) for _ in range(n+1)] for j in range(l+1)]
        # for i in range(1,l+1):
        #     one=strs[i-1].count("1")
        #     zero=strs[i-1].count("0")
        #     for j in range(1,n+1):
        #         for k in range(1,m+1):
        #             if j>=one and k>=zero:
        #                 dp[i][j][k]=max(1+dp[i-1][j-one][k-zero],dp[i-1][j][k])
        #             else:
        #                 dp[i][j][k]=dp[i-1][j][k]
        #     print(dp)            
        #     return dp[-1][-1][-1]            