class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        seti=set(["a","i","e","o","u"])
        while i<j:
            while i<j and s[i].lower() not in seti:
                i+=1
            while i<j and s[j].lower() not in seti:
                j-=1
            if i<j:
                a=s[i]
                b=s[j]
                s=s[:i]+b+s[i+1:j]+a+s[j+1:]
            i+=1
            j-=1
        return s         