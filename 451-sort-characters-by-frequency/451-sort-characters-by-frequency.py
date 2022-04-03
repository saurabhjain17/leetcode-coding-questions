import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dic=Counter(s)
        n=len(dic)
        heap=[]
        for i in dic:
            heapq.heappush(heap,(-dic[i],i))
        op=""
        for i in range(n):
            key,val=heapq.heappop(heap)
            op=op+val*(-key)
        return op    
            