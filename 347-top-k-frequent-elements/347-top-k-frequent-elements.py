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
        ans=[]
        heap=[]
        for i in dic:
            heapq.heappush(heap,(-dic[i],i))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans    