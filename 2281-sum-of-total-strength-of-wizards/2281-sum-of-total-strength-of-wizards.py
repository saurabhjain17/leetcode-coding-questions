class Solution:
    def totalStrength(self, st: List[int]) -> int:
        modi=10**9+7
        n=len(st)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=(prefix[i]+st[i])%modi
        
        sum_prefix=[0]*(n+2)
        for i in range(n+1):
            sum_prefix[i+1]=(prefix[i]+sum_prefix[i])%modi
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and st[stack[-1]] > st[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and st[stack[-1]] >= st[i]:
                left[stack.pop()] = i
            stack.append(i)
        res=0
        for i in range(n):
            res+=((sum_prefix[right[i]+1]-sum_prefix[i+1])*(i-left[i])%modi+modi*2-(sum_prefix[i+1]-sum_prefix[left[i]+1])*(right[i]-i)%modi)%modi*st[i]%modi
            res%=modi
        return int(res)    
            
            
            