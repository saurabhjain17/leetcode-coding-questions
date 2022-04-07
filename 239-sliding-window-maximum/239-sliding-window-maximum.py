import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        n=len(nums)
        op=[]
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
            
        a,ind=heapq.heappop(heap)
        op.append(-a)
        heapq.heappush(heap,(a,ind))
        for i in range(k,n):
            heapq.heappush(heap,(-nums[i],i))
            a,ind=heapq.heappop(heap)
            while i-k>=ind:
                a,ind=heapq.heappop(heap)
            op.append(-a)    
            heapq.heappush(heap,(a,ind))
        return op    