class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        length=1
        ans=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]==prices[i-1]-1:
                length+=1
            else:
                ans+=(length*(length+1))//2
                length=1
        ans+=(length*(length+1))//2
        return ans