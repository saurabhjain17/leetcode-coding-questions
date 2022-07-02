class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        verticalCuts.sort()
        maxi1=verticalCuts[0]-0
        n=len(verticalCuts)
        for i in range(1,n):
            maxi1=max(maxi1,verticalCuts[i]-verticalCuts[i-1])
        maxi2=horizontalCuts[0]-0
        n=len(horizontalCuts)
        for i in range(1,n):
            maxi2=max(maxi2,horizontalCuts[i]-horizontalCuts[i-1])   
        return (maxi1*maxi2)%(1000000007)    