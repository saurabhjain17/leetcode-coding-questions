import math
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        total=0
        n=len(nums)
        for i in range(n):
            gd=nums[i]
            for j in range(i,n):
               gd=math.gcd(nums[j],gd)
               if gd==k:
                    total+=1
        return total            