class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1:
            return 1
        dp=[0]*n
        if ratings[0]<=ratings[1]:
            dp[0]=1
        if ratings[-1]<=ratings[-2]:
            dp[-1]=1
        for i in range(1,n-1):
            if ratings[i]<=ratings[i-1] and  ratings[i]<=ratings[i+1]:
                  dp[i]=1
        for i in range(n):
            if dp[i]==1:
                left=i-1
                right=i+1
                while left>-1 and ratings[left+1]<ratings[left] and dp[left+1]+1>dp[left]:
                    dp[left]=dp[left+1]+1
                    left-=1
                while right<n and ratings[right-1]<ratings[right] and dp[right-1]+1>dp[right]:
                    dp[right]=dp[right-1]+1
                    right+=1
        return sum(dp)            
                    