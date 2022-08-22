class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic={str(i):i for i in range(10)}
        counti=dict()
        for i in num:
            x=dic[i]
            if x not in counti:
                counti[x]=0
            counti[x]+=1
        size=0
        mid=-1
        fir=""
        for i in range(9,0,-1):
            if i in counti:
                fir+=(str(i)*(counti[i]//2))
                if mid==-1:
                    if counti[i]%2==1:
                        mid=i
        if fir!="":
            if 0 in counti:
                fir+=("0"*(counti[0]//2))
                if counti[0]%2==1 and mid==-1:
                    mid=0
        else:
            if mid==-1:
                if 0 in counti:
                    return "0"
            else:
                return str(mid)
        las=fir[::-1]
        if mid==-1:
            return fir+las
        else:
            return fir+str(mid)+las
            