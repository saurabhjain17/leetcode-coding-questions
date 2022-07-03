class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[1]*2 for i in range(n)]
        
        maxi=1
        for i in range(1,n):
            po=ne=0
            for j in range(i-1,-1,-1):
                if nums[j]>nums[i]:
                    ne=max(ne,dp[j][1])
                elif nums[j]<nums[i]:
                    po=max(po,dp[j][0])
            dp[i][1]+=po
            dp[i][0]+=ne
            maxi=max(maxi,dp[i][1],dp[i][0])
        return maxi         