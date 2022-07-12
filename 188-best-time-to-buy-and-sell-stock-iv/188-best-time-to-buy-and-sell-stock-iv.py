class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=dict()
        n=len(prices)
        def rec(prices,n,k,buy,i,dp):
            if i==n or k==0:
                return 0
            if (i,k,buy) not in dp:
                if buy==True:
                    dp[(i,k,buy)]=max(-prices[i]+rec(prices,n,k,False,i+1,dp),rec(prices,n,k,True,i+1,dp))
                else:
                    dp[(i,k,buy)]=max(prices[i]+rec(prices,n,k-1,True,i+1,dp),rec(prices,n,k,False,i+1,dp))
            return dp[(i,k,buy)]       
        return rec(prices,n,k,True,0,dp)            
            