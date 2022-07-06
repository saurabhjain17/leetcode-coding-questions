class Solution:
    def rec(self,s,seti,n,dp,start):
        if start==n:
            return True
        if dp[start]!=-1:
            return dp[start]
        string=""
        ans=False
        for i in range(start,n):
            string+=s[i]
            if string in seti:
                ans=ans or self.rec(s,seti,n,dp,i+1)
                
                if ans==True:
                    dp[start]=ans
                    return True
        dp[start]=ans        
        return False        
                
                
           
                
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        seti=set(wordDict)       
        dp=[-1]*(n+1)
        return self.rec(s,seti,n,dp,0)
        