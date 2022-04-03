class Solution:
    def dis(self,candies,mid,k,n):
        
        i=0
        while k>0 and i<n:
            k-=candies[i]//mid
            i+=1
        if  k<=0:
            return True
        return False
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sumi=sum(candies)
        if sumi<=k:
            return sumi//k
        n=len(candies)
        lo=1
        hi=max(candies)
        op=0
        while lo<=hi:
            if hi-lo==1:
                if self.dis(candies,hi,k,n):
                    return hi
                return lo
            if lo==hi:
                return lo
            mid=(lo+hi)//2
            
            if self.dis(candies,mid,k,n):
                
                lo=mid
            else:
                hi=mid-1
        return lo        