class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[-1]*(n) for i in range(n)]
        for i in range(n):
            dp[i][i]=1
        mid=1
        while mid<n:
            left=mid-1
            right=mid+1
            while left>-1 and right<n:
                if dp[left][right]==0 or dp[left][right]==1:
                    break
                if s[left]!=s[right]:
                        dp[left][right]=0
                        break
                else:       
                    dp[left][right]=1&dp[left+1][right-1]
                left-=1
                right+=1
            left=mid-1
            right=mid
            while left>-1 and right<n:
                if dp[left][right]==0 or dp[left][right]==1:
                    break
                if left+1==right and s[left]==s[right]:
                        dp[left][right]=1  
                if s[left]!=s[right]:
                        dp[left][right]=0
                        break
                else:       
                    dp[left][right]=1&dp[left+1][right-1]
                left-=1
                right+=1
            mid+=1   
        # print(dp)    
        def rec(s,start,n,tem,dp):
            global ans
            if start==n:
                ans.append(tem.copy())
                return
            for i in range(start,n):
                if dp[start][i]==1:
                    tem.append(s[start:i+1])
                    rec(s,i+1,n,tem,dp)
                    tem.pop(-1)
                    
        global ans
        ans=[]
        rec(s,0,n,[],dp)
        return ans