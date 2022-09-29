import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        ans=[]
        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        ans.sort()
        return ans