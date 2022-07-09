import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heap=[]
        dp=[0]*n
        dp[0]=nums[0]
        heapq.heappush(heap,(-dp[0],0))
        for i in range(1,n):
            
            val,ind=heapq.heappop(heap)
            while ind<i-k:
                val,ind=heapq.heappop(heap)
            dp[i]=nums[i]-val
            heapq.heappush(heap,(-dp[i],i))
            heapq.heappush(heap,(val,ind))
        return dp[-1]    