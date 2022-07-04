class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        hi=max(piles)
        ans=min(piles)
        def ispossible(piles,mid,hour):
            for i in piles:
                a=i%mid
                hour-=i//mid
                if a>0:
                    hour-=1
                if hour<0:
                    return False
            # if mid==4:
            #     print(hour)
            if hour>=0:
                return True
            return False
            
        while l<=hi:
            mid=(l+hi)//2
            # print(mid)
            if ispossible(piles,mid,h):
                
                ans=mid
                hi=mid-1
            else:
                l=mid+1
        return ans        