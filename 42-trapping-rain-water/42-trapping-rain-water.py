class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        maxi=0
        for i in range(1,n):
            left[i]=max(maxi,height[i-1])
            maxi=max(height[i-1],maxi)
        maxi=0    
        for i in range(n-2,-1,-1):
            right[i]=max(maxi,height[i+1])
            maxi=max(height[i+1],maxi) 
        total=0
        for i in range(1,n-1):
            if min(left[i],right[i])-height[i]>0:
                total+=min(left[i],right[i])-height[i]
        return total        
            