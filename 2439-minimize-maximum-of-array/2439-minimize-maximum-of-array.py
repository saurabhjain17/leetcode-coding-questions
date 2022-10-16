import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        
        pre=[nums[0]]
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        maxi=min(nums)
        for i in range(n-1,0,-1):
            avg=math.ceil((pre[i-1]+nums[i])/(i+1))
            if nums[i]>avg:
                t=nums[i]-avg
                nums[i-1]+=t
                nums[i]=avg
        return max(nums)        