from heapq import heappush,heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq=[]
        trips.sort(key=lambda x:x[1])
        for u,v,w in trips:
            if capacity<u:
                while pq  and pq[0][0]<=v:
                    a,b=heappop(pq)
                    capacity+=b
                if capacity<u:
                    return False
                
            capacity-=u
            heappush(pq,(w,u))
               
        return True         