class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        op=[]
        def comb(k,n,i,op,tem,last):
            if i==k:
                if n==0:
                    op.append(tem.copy())
                return
            for j in range(last+1,10):
                if j<=n:
                    tem.append(j)
                    comb(k,n-j,i+1,op,tem,j)
                    tem.pop(-1)
        comb(k,n,0,op,[],0)  
        return op