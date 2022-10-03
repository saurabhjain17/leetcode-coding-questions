import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        size=1
        out=0
        heap=[neededTime[0]]
        for i in range(1,n):
            if colors[i]==colors[i-1]:
                heapq.heappush(heap,neededTime[i])
                size+=1
            else:
                while size>1:
                    out+=heapq.heappop(heap)
                    size-=1
                heap=[neededTime[i]]
                size=1
        while size>1:
                out+=heapq.heappop(heap)
                size-=1  
        return out        