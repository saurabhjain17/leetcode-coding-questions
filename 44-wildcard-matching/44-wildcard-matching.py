class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        dp=[[-1]*(m+1) for i in range(n+1)]
        def rec(dp,s,p,n,m):
            if n==0 :
                if m==0 or p[:m].count("*")==m:
                    return True
            if n==0 or m==0:
                return False
            if dp[n][m]==-1:
                if s[n-1]==p[m-1] or p[m-1]=="?":
                    dp[n][m]=rec(dp,s,p,n-1,m-1)
                elif p[m-1]=="*":
                    dp[n][m]=rec(dp,s,p,n-1,m) or rec(dp,s,p,n,m-1)
                else:
                    dp[n][m]=False
            return dp[n][m]
        return rec(dp,s,p,n,m)