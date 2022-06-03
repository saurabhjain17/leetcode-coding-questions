class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n=len(heights)
        right=[-1]*n
        left=[-1]*n
        stack=[n-1]
        p=1
        for i in range(n-2,-1,-1):
            while p and heights[stack[-1]]>=heights[i]:
                stack.pop(-1)
                p-=1
            if p>0:
                right[i]=stack[-1]
                
            
            stack.append(i)
            p+=1
        stack=[0]
        p=1
        for i in range(1,n):
            while p and heights[stack[-1]]>=heights[i]:
                stack.pop(-1)
                p-=1
            if p>0:
                left[i]=stack[-1]
            stack.append(i)
            p+=1
        maxi=0
        for i in range(n):
            lefti=max(0,left[i]+1)
            righti=n-1
            if right[i]!=-1:
                righti=right[i]-1
            maxi=max(maxi,heights[i]*(righti-lefti+1))
        return maxi    
        
                