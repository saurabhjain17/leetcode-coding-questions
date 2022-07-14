class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        counti=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i] and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    counti[i]=counti[j]
                elif nums[j]<nums[i] and 1+dp[j]==dp[i]:   
                    counti[i]+=counti[j]
        maxi=max(dp)
        total=0
        for i in range(n):
            if dp[i]==maxi:
                total+=counti[i]
        return total        