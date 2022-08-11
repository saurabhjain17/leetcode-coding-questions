import math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic=dict()
        n=len(nums)
        count=0
        size=0
        for i in nums:
            p=math.gcd(i,k)
            if p not in dic:
                dic[p]=0
            for j in dic:
                if (j*p)%k==0:
                    count+=dic[j]
            dic[p]+=1
        return count    
        
                