import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(spells)
        m=len(potions)
        dp=[0]*n
        for i in range(n):
            if potions[m-1]*spells[i]>=success:
                fin=math.ceil(success/spells[i])
                low=0
                high=m-1
                ans=m-1
                while low<=high:
                    mid=(low+high)//2
                    if potions[mid]>=fin:
                        ans=mid
                        high=mid-1
                    else:
                        low=mid+1
                dp[i]=m-ans
        return dp        