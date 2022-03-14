class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*60
        dp[2]=1
        dp[3]=2
        dp[4]=4
        dp[5]=6
        dp[6]=9
        dp[7]=12
        dp[8]=18
        dp[9]=27
        dp[10]=36
        if n<=10:
            return dp[n]
        for i in range(11,n+1):
            op=1
            k=i
            while i>4:
                i-=3
                op*=3
            op*=i
            dp[k]=op
        return dp[n]    