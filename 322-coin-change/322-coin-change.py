class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n+1)]
        
        for i in range(1,amount+1):
            dp[0][i]=math.inf
            if i%coins[0]==0:
                dp[1][i]=i//coins[0]
            else:
                dp[1][i]=math.inf
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[n][amount]==math.inf:
            return -1
        return dp[n][amount]
        # n=len(coins)
        # dp=[[0]*(amount+1) for i in range(n+1)]
        # for i in range(1,amount+1):
        #     dp[0][i]=float("inf")
        #     if i%coins[0]==0:
        #         dp[1][i]=i//coins[0]
        #     else:
        #         dp[1][i]=float("inf")
        # for i in range(2,n+1):
        #     for j in range(1,amount+1):
        #         if coins[i-1]<=j:
        #             dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        #         else:
        #             dp[i][j]=dp[i-1][j]
        # if dp[n][amount]==float("inf"):
        #     return -1
        # return dp[n][amount]        