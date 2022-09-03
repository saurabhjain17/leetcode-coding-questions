class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        out=set()
        def rec(length,K,number):
            if length==0:
                out.add(number)
                return
            for i in range(10):
                if abs(i-number%10)==K:
                    rec(length-1,K,number*10+i)
        for i in range(1,10):
            rec(n-1,k,i)
        return(list(out))    
        