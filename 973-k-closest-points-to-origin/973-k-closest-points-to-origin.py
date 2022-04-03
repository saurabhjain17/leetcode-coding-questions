import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        n=len(points)
        for i in range(k):
            dis=(points[i][0]**2 +points[i][1]**2)
            heapq.heappush(heap,(-dis,points[i]))
        for i in range(k,n):
            dis=(points[i][0]**2 +points[i][1]**2)
            heapq.heappushpop(heap,(-dis,points[i]))
        op=[]
        for i in range (k):    
            dis,point=heapq.heappop(heap)
            op.append(point)
        return op    