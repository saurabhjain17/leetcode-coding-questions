class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        ans=1e20
        zero=s.count("0")
        # if zero*2!=n:
        #     return -1
        lis=["1"]*n
        for i in range(0,n,2):
            lis[i]="0"
        ans1=0
        zero=[]
        one=[]
        for i in range(n):
            if s[i]=="1" and lis[i]=="0":
                zero.append(i)
            elif s[i]=="0" and lis[i]=="1":
                one.append(i)
        if len(zero)==len(one):
            ans=len(zero)
        lis=["0"]*n
        for i in range(0,n,2):
            lis[i]="1"
        zero=[]
        one=[]
        for i in range(n):
            if s[i]=="1" and lis[i]=="0":
                zero.append(i)
            elif s[i]=="0" and lis[i]=="1":
                one.append(i)  
        if len(zero)==len(one):
            ans= min(ans,len(zero))
        if ans==1e20:
            return -1
        return ans