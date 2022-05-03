import math
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        fir=las=-1
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            if nums[0]>nums[1]:
                return 2
            return 0
        mini=math.inf
        maxi=-math.inf
        for i in range(1,n):
            if fir==-1:
                if nums[i]<nums[i-1]:
                    fir=i-1
                    mini=min(mini,nums[i])
            else:
                mini=min(mini,nums[i])
        for i in range(n-2,-1,-1):
            if las==-1:
                if nums[i]>nums[i+1]:
                    las=i+1
                    maxi=max(maxi,nums[i])
            else:
                maxi=max(maxi,nums[i])
        print(fir,las)       
        ind=ind2=-1        
        for i in range(fir+1):
            if nums[i]>mini:
                ind=i
                break
        for i in range(n-1,-1,-1):
            if nums[i]<maxi:
                ind2=i+1
                break
                
        return ind2-ind
       