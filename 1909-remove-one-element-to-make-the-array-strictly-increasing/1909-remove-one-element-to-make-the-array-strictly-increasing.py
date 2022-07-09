class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        x=0
        n=len(nums)
        i=0
        j=1
        while j<n and x<2:
            if nums[j]>nums[i]:
                i=j
                j+=1
                continue
            else:
                if x==1:
                    return False
                if i==0 or nums[i-1]<nums[j]:
                    x+=1
                    i=j
                else:
                    x+=1
                    
                j+=1
        if x<2:
            return True
        return False
                