class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n=len(s)
        counti=s.count("0")
        i=n-1
        val=0
        power=1
        while i>-1 and val+power<=k:
            if s[i]=="1":
                counti+=1
                val+=power
            power<<=1
            i-=1
        return counti    
                