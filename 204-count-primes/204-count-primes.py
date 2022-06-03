class Solution:
    
    def countPrimes(self, n: int) -> int:
      
        dp=[False]*(n)
        if n<3:
            return 0
        counti=0
        for i in range(2,min(int(n**.5)+3,n)):
            if dp[i]==False:
                
                j=i*i
                while j<n:
                    dp[j]=True
                    j+=i
        for i in range(2,n):
            if dp[i]==False:
                counti+=1
        return counti            