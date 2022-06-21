import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        n=len(heights)
        i=1
        if ladders>=n-1:
            return n-1
        while i<n and (ladders>0 or heights[i]-heights[i-1]<=bricks or heights[i]-heights[i-1]<=0):
            t=heights[i]-heights[i-1]
            if t<=0:
                i+=1
                continue
            else:
                if bricks>=t:
                    bricks-=t
                    heapq.heappush(heap,-t)
                else:
                    bricks-=t
                    heapq.heappush(heap,-t)
                    m=-heapq.heappop(heap)
                    bricks+=m
                    ladders-=1
                i+=1
        return i-1       
                    