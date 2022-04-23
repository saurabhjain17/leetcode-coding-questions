class Solution:
    dic={"1":1,"0":0,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    def myAtoi(self, s: str) -> int:
        
        i=0
        n=len(s)
        while i<n and s[i]==" ":
            i+=1
        sign=1
        if i<n and s[i]=="-":
            sign=-1
            i+=1
        elif i<n and s[i]=="+":
            sign=1
            i+=1
        ans=0    
        while i<n and s[i] in Solution.dic:
            ans=ans*10+Solution.dic[s[i]]
            i+=1
        ans= ans*sign 
        ans=min(ans,2**31-1)
        ans=max(ans,-2**31)
        return ans
            