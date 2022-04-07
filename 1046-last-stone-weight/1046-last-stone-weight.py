import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        n=0
        for i in stones:
            heapq.heappush(heap,-i)
            n+=1
        while n>1:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            n-=2
            c=abs(a-b)
            if c!=0:
                heapq.heappush(heap,-c)
                n+=1
        if n==0:
            return 0
        else:
            return -heapq.heappop(heap)