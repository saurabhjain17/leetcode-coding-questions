class Solution:
    def ispossible(self,weights,cap,days,n):
        total=0
        for i in range(n):
            if total+weights[i]<=cap:
                total+=weights[i]
            else:
                total=weights[i]
                days-=1
        if days>0:
            return True
        return False
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumi=sum(weights)
        n=len(weights)
        lo=max(weights)
        hi=sumi
        ans=hi
        while lo<=hi:
            mid=(lo+hi)//2
            if self.ispossible(weights,mid,days,n):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans        