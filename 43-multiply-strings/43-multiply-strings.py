class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={str(x):x for x in range(10)}
        n=len(num2)
        m=len(num1)
        op=""
        ans=0
        carry=0
        for i in range(n-1,-1,-1):
            tem=0
            carry=0
            k=1
            for j in range(m-1,-1,-1):
                numb=dic[num1[j]]*dic[num2[i]]
                numb+=carry
                if numb<10:
                    carry=0
                    
                else:
                    carry=int(str(numb)[0])
                    numb=int(str(numb)[1:])
                tem+=numb*k
                k*=10
            if carry>0:
                tem+=carry*k
            # print(tem)    
            ans+=tem
            # print(ans)
            op+=str(ans%10)
            # print(op)
            ans//=10
        # print(carry) 
        op=op[::-1]
        if ans>0:
            op=str(ans)+op
        return str(int(op))    