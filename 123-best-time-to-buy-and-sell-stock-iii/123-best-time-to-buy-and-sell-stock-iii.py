class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=[0]*n
        max_price=prices[n-1]
        for i in range(n-2,-1,-1):
            max_price=max(max_price,prices[i])
            profit[i]=max(profit[i+1],max_price-prices[i])
        min_price=prices[0]
        for i in range(1,n):
            min_price=min(min_price,prices[i])
            profit[i]=max(profit[i-1], profit[i]+(prices[i]-min_price))
        return profit[n-1]    