class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        m=n//2
        if n==1:
            return ""
        for i in range(m):
            if palindrome[i]!="a":
                return palindrome[:i]+"a"+palindrome[i+1:]
        return palindrome[:-1]+"b"    