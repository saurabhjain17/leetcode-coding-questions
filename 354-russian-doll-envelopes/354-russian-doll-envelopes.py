class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp=[]
        n=len(envelopes)
        m=1
        def fin(val,dp,m):
            i=0
            j=m-1
            op=-1
            while i<=j:
                mid=(i+j)//2
                if dp[mid][0]<val[0] and dp[mid][1]<val[1]:
                    op=mid
                    i=mid+1
                else:
                    j=mid-1
            return op+1        
        dp.append(envelopes[0])
        for i in range(1,n):
            if dp[-1][0]<envelopes[i][0] and dp[-1][1]<envelopes[i][1]:
                dp.append(envelopes[i])
                m+=1
                
            else:
                ind=fin(envelopes[i],dp,m)
                dp[ind]=envelopes[i]
        print(dp)        
        return m        
        