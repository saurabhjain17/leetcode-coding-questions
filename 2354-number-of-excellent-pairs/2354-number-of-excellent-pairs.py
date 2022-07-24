class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        n=len(nums)
        dp=[0]*n
        for i in range(n):
            x=nums[i]
            counti=0
            while x:
                x&=(x-1)
                counti+=1
            dp[i]=counti
        # print(dp)    
        dp.sort()    
        ans=0
        for i in range(n):
            low=i
            high=n-1
            ind=n
            while low<=high:
                mid=(low+high)//2
                if dp[i]+dp[mid]>=k:
                    ind=mid
                    high=mid-1
                else:
                    low=mid+1
            tem=2*(n-ind)
            if dp[i]+dp[i]>=k:
                tem-=1
            ans+=tem    
        return ans    
                    