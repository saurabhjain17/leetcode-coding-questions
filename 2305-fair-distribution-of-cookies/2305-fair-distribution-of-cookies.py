class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        tem=[0]*k
        n=len(cookies)
        dp=[-1]*(n+1)
        global ans
        ans=sum(cookies)
        def rec(cookies,n,dp,tem,k):
            global ans
            if n==0:
                ans=min(ans,max(tem))
                return
                # return max(tem)
            # if dp[n]!=-1:
            #     return dp[n]
            # mini=math.inf
            for i in range(k):
                tem[i]+=cookies[n-1]
                # mini=min(mini,rec(cookies,n-1,dp,tem,k))
                rec(cookies,n-1,dp,tem,k)
                tem[i]-=cookies[n-1]
                if tem[i]==0:
                    break
            # dp[n]=mini
            # return dp[n]
            
            
        op= rec(cookies,n,dp,tem,k)
        # print(dp)
        return ans