class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxi=0
        length=0
        prod=1
        for i in nums:
            
            if i==0:
                prod=0
            elif i<0:
                prod*=-1
            length+=1
            if prod==0:
                prod=1
                length=0
            elif prod>0:
                maxi=max(length,maxi)
        length=0
        n=len(nums)
        prod=1
        for j in range(n-1,-1,-1):
            i=nums[j]
            if i==0:
                prod=0
            elif i<0:
                prod*=-1
            length+=1
            if prod==0:
                prod=1
                length=0
            elif prod>0:
                maxi=max(length,maxi) 
        return maxi       