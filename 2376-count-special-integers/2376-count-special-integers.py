class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        length=len(str(n))-1
        counti=0
        size=1
        
        power=81
        nm=9
        while size<=length:
            if size==1:
                counti+=9
                size+=1
            elif size==2  :
                counti+=81
                size+=1
            else:
                power=(power*(nm-1))
                counti+=power
               
                nm-=1
                size+=1
      
        dp=[]
        j=n
        prod=1
        
        while j>0:
            dp.append(j%10)
            j//=10
        dp.reverse()
        length=len(dp)
        nm=9
        for i in range(length-1):
            prod*=nm
            nm-=1
        nm=9    
        seti=set()
        for i in range(length):
            start=0
            if i==0:
                start=1
            if i==0 and dp[0]==1:
                 seti.add(1)
                 prod//=nm
                 nm-=1
                 continue
            for j in range(start,dp[i]):
                # print(counti,prod,j,i)
                # print(seti)
                if j not in seti:
                    counti+=prod
            prod//=nm
            nm-=1
            if dp[i] in seti:
                break
            seti.add(dp[i])
        seti=set()
        for i in str(n):
            seti.add(i)
        if len(seti)==len(str(n)):
            counti+=1
        return counti    
            
                
                