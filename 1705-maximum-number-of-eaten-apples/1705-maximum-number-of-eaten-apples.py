import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap=[]
        counti=0
        n=len(apples)
        j=0
        for i in range(n):
            j=i+1
            heapq.heappush(heap,(i+days[i],apples[i]))
            while heap and (heap[0][1]==0 or heap[0][0]<=i):
                heapq.heappop(heap)
            if heap :
                counti+=1
                u,v=heapq.heappop(heap)
                v-=1
                if v>0:
                    heapq.heappush(heap,(u,v))
        while heap:
            u,v=heapq.heappop(heap)
            if v>0 and u>j:
                counti+=min(v,u-j)
                j+=min(v,u-j)
        return counti        
            