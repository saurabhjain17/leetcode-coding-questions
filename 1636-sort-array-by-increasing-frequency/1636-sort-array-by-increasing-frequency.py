import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dic=dict()
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        heap=[]
        heapq.heapify(heap)
        for i in dic:
            heapq.heappush(heap,(dic[i],-i))
        i=0
        while i<n:
            key,value=heapq.heappop(heap)
            for j in range(key):
                nums[i]=-value
                i+=1
        return nums        