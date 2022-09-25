class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=1
        maxi=max(nums)
        leg=0
        for i in nums:
            if i==maxi:
                leg+=1
                ans=max(ans,leg)
            else:
                leg=0
        return ans        