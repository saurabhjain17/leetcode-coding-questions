class Solution:
    
    def countPrimes(self, n: int) -> int:
      
        dp=[False]*(n)
        if n<2:
            return 0
        counti=0
        for i in range(2,n):
            if dp[i]==False:
                counti+=1
                j=i+i
                while j<n:
                    dp[j]=True
                    j+=i
        return counti            