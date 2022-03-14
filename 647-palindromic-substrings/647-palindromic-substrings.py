class Solution:
    def countSubstrings(self, s: str) -> int:
        counti=1
        n=len(s)
        for i in range(1,n):
            left=i
            right=i
            while left>-1 and right<n and  s[left]==s[right]:
                counti+=1
                left-=1
                right+=1
            left=i-1
            right=i
            while left>-1 and right<n and  s[left]==s[right]:
                counti+=1
                left-=1
                right+=1
        return counti        