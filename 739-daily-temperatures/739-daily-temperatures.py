class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        n=len(temp)
        out=[0]*n
        stack=[n-1]
        for i in range(n-2,-1,-1):
            while stack and temp[i]>=temp[stack[-1]]:
                stack.pop(-1)
            if stack:
                out[i]=(stack[-1]-i)
            stack.append(i)
        return out    
                
                