class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> List[str]:
        global ans
        n=len(dic)
        ans=[]
        seti=set(dic)
        length=len(s)
        dp=[[0]*(length+1) for i in range(length+1)]
        for i in range(length):
            for j in range(i,length):
                if s[i:j+1] in seti:
                    dp[i][j]=1
        def rec(dp,s,seti,start,length,tem):
            global ans
            if start==length:
                 ans.append(tem[:-1])
                 
                 return
            string="" 
            for i in range(start,length):
                string+=s[i]
                if dp[start][i]==1:
                   
                   rec(dp,s,seti,i+1,length,tem+string+" ")
                # else:
                #     rec(dp,s,seti,i+1,length,tem)
                   
        rec(dp,s,seti,0,length,"")
        return ans