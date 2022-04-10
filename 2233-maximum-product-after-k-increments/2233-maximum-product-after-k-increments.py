import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        p=(10**9+7)
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappush(nums,(heapq.heappop(nums)+1))
        op=1
        for i in nums:
            op*=i
            op%=p
        return op    
            