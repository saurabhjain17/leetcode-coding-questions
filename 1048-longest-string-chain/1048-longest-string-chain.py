class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        def isvalid(words,n,i,j,length,ln):
            p=0
            q=0
            while p<length and q<ln:
                if words[i][p]==words[j][q]:
                    q+=1
                p+=1
            if q>=ln:
                return True
            return False
                    
        dp=[1]*n
        words.sort(key=lambda x:len(x))
        maxii=len(words[-1])-len(words[0])+1
        if maxii==1:
            return maxii
        maxi=1
        l=len(words[0])
        op=0
        for i in range(1,n):
            length=len(words[i])
            if length!=l:
                ot=0
                for j in range(i-1,-1,-1):
                    ln=len(words[j])
                    if ln==length:
                        continue
                    elif length-ln>1:
                        break
                    else:
                        if isvalid(words,n,i,j,length,ln):
                            ot=max(ot,dp[j])
                dp[i]+=ot
            if dp[i]==maxii:
                return maxii
            maxi=max(maxi,dp[i])
        return maxi    
            
                