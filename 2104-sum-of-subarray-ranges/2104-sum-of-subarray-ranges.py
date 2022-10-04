class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sumi=0
        n=len(nums)
        for i in range(n):
            mini=maxi=nums[i]
            for j in range(i+1,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                sumi+=(maxi-mini)
        return sumi        