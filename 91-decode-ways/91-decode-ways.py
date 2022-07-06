class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+1)
        def rec(ind,n,s,dp):
            if ind==n:
                return 1
            if ind==n-1:
                if s[ind]=="0":
                    return 0
                else:
                    return 1
            
            if dp[ind]!=-1:
                return dp[ind]
            if s[ind]=="0":
                
                dp[ind]=0
            else:
                ans=rec(ind+1,n,s,dp)
                if int(s[ind:ind+2])<27:
                    ans+=rec(ind+2,n,s,dp)
                dp[ind]=ans
            return dp[ind]
           
        op=rec(0,n,s,dp)
   
        return op
                    
                