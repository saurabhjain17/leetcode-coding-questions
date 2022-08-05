class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return num
        if num>-10 and num<10:
            return num
        neg=0
        if num<0:
            neg=1
            num*=-1
        val=[]
        while num>0:
            val.append(str(num%10))
            num//=10
        val.sort()    
        if neg:
           
            val=val[::-1]
            return -int("".join(val))
        if val[0]!="0":
            return int("".join(val))
        for i in range(len(val)):
            if val[i]!="0":
                ind=i
                break
        return int("".join([val[ind]]+val[:ind]+val[ind+1:]))
    