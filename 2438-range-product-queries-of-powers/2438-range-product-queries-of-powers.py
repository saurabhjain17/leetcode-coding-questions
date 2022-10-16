class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x=bin(n)[2:]
        modu=10**9+7
        lis=[]
        x=x[::-1]
        ind=0
        for i in x:
            if i=="1":
                lis.append(2**ind)
            ind+=1
        ans=[]
        for left,right in queries:
            val=1
            for i in range(left,right+1):
                val*=lis[i]
            ans.append(val%modu)
        return ans    
            
        