class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        dic={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
        # op=[1]*n
        # k=k-n
        # i=n-1
        # while k>0 and i>-1:
        #     if k>=25:
        #         op[i]+=25
        #         k-=25
        #     elif k<25 and k>0:
        #         op[i]+=k
        #         k=0
        #     i-=1
        # ans=""
        # for i in op:
        #     ans+=dic[i]
        # return ans    
       
    
    ####method 2
        # reserve=n
        # k=k-n
        # length=0
        # ans=""
        # while k>0:
        #     if k>=25:
        #         ans="z"+ans
        #         k-=25
        #         length+=1
        #     elif k>0 and k<25:
        #         ans=dic[1+k]+ans
        #         k=0
        #         length+=1
        # op="a"*(reserve-length)+ans
        # return op
        
        ####method 3
        reserve=n
        k=k-n
        length=k//25
        remain=k%25
        additional=0
        addi=""
        if remain>0:
            additional+=1
            addi=dic[1+remain]
        
        # while k>0:
        #     if k>=25:
        #         ans="z"+ans
        #         k-=25
        #         length+=1
        #     elif k>0 and k<25:
        #         ans=dic[1+k]+ans
        #         k=0
        #         length+=1
        op="a"*(reserve-length-additional)+addi+"z"*length
        return op
        