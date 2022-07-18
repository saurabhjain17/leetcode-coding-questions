import heapq
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n=len(nums)
        for i in range(n):
            nums[i]=int(nums[i])
        m=len(queries)
        ans=[-1]*m
        for i in range(m):
            k,trim=queries[i]
            heap=[]
            po=10**trim
            for j in range(n):
                heapq.heappush(heap,(nums[j]%po,j))
            for j in range(k):
                nod,ind=heapq.heappop(heap)
            ans[i]=ind
        return ans    