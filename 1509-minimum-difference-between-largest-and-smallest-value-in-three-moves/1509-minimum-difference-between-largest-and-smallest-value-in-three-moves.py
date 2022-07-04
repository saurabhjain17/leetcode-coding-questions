import math
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=4:
            return 0
        nums.sort()
        maxi=math.inf
        for i in range(4):
            maxi=min(maxi,nums[n-4+i]-nums[i])
        # print(nums)    
        return maxi    