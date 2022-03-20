class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_swap=float("inf")
        n=len(tops)
        for i in range(1,7):
            top=bot=0
            for j in range(n):
                if tops[j]==bottoms[j] and tops[j]==i:
                    continue
                elif tops[j]==i:
                    bot+=1
                elif bottoms[j]==i:
                    top+=1
                else:
                    break
                    
            if j==n-1: 
                
                min_swap=min(min_swap,min(top,bot))
        if min_swap== float("inf"):
            return -1
        return min_swap