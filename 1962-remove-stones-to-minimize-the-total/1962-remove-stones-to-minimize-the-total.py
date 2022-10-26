from math import ceil
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        lis=[-a for a in piles]
        heapq.heapify(lis)
        for i in range(k):
            a=-heapq.heappop(lis)
            heapq.heappush(lis,-ceil(a/2))
        return -sum(lis)    