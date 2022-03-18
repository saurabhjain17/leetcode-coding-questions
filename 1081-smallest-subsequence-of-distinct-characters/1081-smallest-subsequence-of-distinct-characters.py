class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        seen=[0]*(26)
        last=[-1]*(26)
        n=len(s)
        for i in range(n-1,-1,-1):
            if last[ord(s[i])-97]==-1:
                last[ord(s[i])-97]=i
        i=0
        
        while i<n:
            if seen[ord(s[i])-97]==1:
                i+=1
                continue
            elif not stack:
                stack.append(s[i])
                seen[ord(s[i])-97]=1
            else:
                while stack and stack[-1]>s[i] and last[ord(stack[-1])-97]>i:
                    p=stack.pop(-1)
                    seen[ord(p)-97]=0  
                stack.append(s[i]) 
                seen[ord(s[i])-97]=1
            i+=1
        return "".join(stack)     