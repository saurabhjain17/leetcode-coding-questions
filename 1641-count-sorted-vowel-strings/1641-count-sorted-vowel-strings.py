class Solution:
    def countVowelStrings(self, n: int) -> int:
        def con(n,i):
            if n==0:
                return 1
            counti=0
            for j in range(i,5):
                counti+=con(n-1,j)
            return counti
        return con(n,0)