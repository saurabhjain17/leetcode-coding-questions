# import queue
# from queue import priorityQueue
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        t=k    
        heap=[]
        heapq.heapify(heap)
        for i in dic:
            if t>0:
                heapq.heappush(heap,(dic[i],i))
                t-=1
            else:
                key,value=heapq.heappop(heap)
                if key>dic[i]:
                    heapq.heappush(heap,(key,value))
                else:
                    heapq.heappush(heap,(dic[i],i))
        op=[]    
        for i in range(k):
            key,value=heapq.heappop(heap)
            op.append(value)
        return op    