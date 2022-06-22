class Solution:
    def countAndSay(self, m: int) -> str:
        def rec(n):
           
            s=str(n)
            
            op=""
            t=len(s)
            z=s[0]
            counti=1
            for i in range(1,t):
                if s[i]==z:
                    counti+=1
                else:
                    op+=str(counti)+z
                    z=s[i]
                    counti=1
            op+=str(counti)+z      
            return int(op)
        x=1
        if m==1:
            return "1"
        for i in range(1,m):
            x=rec(x)
        return str(x)    