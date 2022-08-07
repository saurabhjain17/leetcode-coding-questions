import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rang=1e10
        start=1e10
        end=1e10
        heap=[]
        maxi=-1e10
        n=len(nums)
        m=len(nums[0])
        for i in range(n):
            heapq.heappush(heap,(nums[i][0],i,0))
            maxi=max(maxi,nums[i][0])
        while heap:
            mini,ro,co=heapq.heappop(heap)
            if rang>maxi-mini:
                rang=maxi-mini
                end=maxi
                start=mini
            if co+1<len(nums[ro]):
                maxi=max(maxi,nums[ro][co+1])
                heapq.heappush(heap,(nums[ro][co+1],ro,co+1))
            else:
                break
        return [start,end]         