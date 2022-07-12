class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=dict()
        n=len(prices)
        def rec(i,buy):
            if i>=n :
                return 0
            if (i,buy) not in dp:
                if buy:
                    dp[(i,buy)]=max(-prices[i]+rec(i+1,False),rec(i+1,True))
                else:
                    dp[(i,buy)]=max(prices[i]-fee+rec(i+1,True),rec(i+1,False))
            return dp[(i,buy)] 
        return rec(0,True)