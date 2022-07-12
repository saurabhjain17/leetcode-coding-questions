class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp=dict()
        def rec(s,n,i,point,dp):
            if n==i:
                if point==0:
                    return True
                return False
            if point<0:
                return False
            if (i,point) not in dp:
                t=False
                if s[i]=="(":
                    t= rec(s,n,i+1,point+1,dp)
                elif s[i]==")":
                    t= rec(s,n,i+1,point-1,dp)
                else:
                    t=  rec(s,n,i+1,point+1,dp) or rec(s,n,i+1,point-1,dp) or rec(s,n,i+1,point,dp)
                dp[(i,point)]=t
            return dp[(i,point)]    
        return rec(s,n,0,0,dp)