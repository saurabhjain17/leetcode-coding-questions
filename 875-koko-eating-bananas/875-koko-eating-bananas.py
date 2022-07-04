class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l=1
#         hi=max(piles)
#         ans=min(piles)
#         def ispossible(piles,mid,hour):
#             for i in piles:
#                 a=i%mid
#                 hour-=i//mid
#                 if a>0:
#                     hour-=1
#                 if hour<0:
#                     return False
#             # if mid==4:
#             #     print(hour)
#             if hour>=0:
#                 return True
#             return False
            
#         while l<=hi:
#             mid=(l+hi)//2
#             # print(mid)
#             if ispossible(piles,mid,h):
                
#                 ans=mid
#                 hi=mid-1
#             else:
#                 l=mid+1
#         return ans     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right