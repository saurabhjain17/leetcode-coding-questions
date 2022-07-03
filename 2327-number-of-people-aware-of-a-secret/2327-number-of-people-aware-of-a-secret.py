class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        for ind in range(2,n+1):
            counti=0
            if ind-delay>=1:
                start=ind-delay
                end=max(0,ind-forget)
                for j in range(start,end,-1):
                    counti+=dp[j]
                dp[ind]=counti
        start=n-forget+1
        # print(dp)
        return sum(dp[start:])%(1000000007)