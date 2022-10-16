class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seti=set(nums)
        ans=-1
        for i in nums:
            if i>0 and -i in seti:
                ans=max(ans,i)
        return ans        