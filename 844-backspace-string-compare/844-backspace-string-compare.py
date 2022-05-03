class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)
        i=m-1
        j=n-1
        while j>-1 and i>-1:
            sp1=sp2=0
            while i>-1 and (sp1>0 or s[i]=="#"):
                if s[i]=="#":
                    sp1+=1
                else:
                    sp1-=1
                i-=1
            
            while j>-1 and (sp2>0 or t[j]=="#"):
                if t[j]=="#":
                    sp2+=1
                else:
                    sp2-=1
                j-=1
            if i>-1 and j>-1:
                if s[i]!=t[j]:
                    return False
                i-=1
                j-=1
        sp1=sp2=0
        while i>-1 and (sp1>0 or s[i]=="#"):
            if s[i]=="#":
                sp1+=1
            else:
                sp1-=1
            i-=1

        while j>-1 and (sp2>0 or t[j]=="#"):
            if t[j]=="#":
                sp2+=1
            else:
                sp2-=1
            j-=1   
        if i==-1 and j==-1:
            return True
        return False

