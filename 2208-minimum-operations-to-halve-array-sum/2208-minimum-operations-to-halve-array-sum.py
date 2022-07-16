import heapq
class Solution:
    # def halveArray(self, nums: List[int]) -> int:
    #     n=len(nums)
    #     sumi=sum(nums)
    #     sumi_want=sumi
    #     for i in range(n):
    #         nums[i]=-nums[i]
    #     heapq.heapify(nums)
    #     counti=0
    #     while sumi_want*2>sumi:
    #         counti+=1
    #         number=-heapq.heappop(nums)
    #         sumi_want-=number
    #         number/=2
    #         sumi_want+=number
    #         heapq.heappush(nums,-number)
    #     return counti    
    def halveArray(self, nums: List[int]) -> int:
        # Creating empty heap
        maxHeap = []
        heapify(maxHeap) # Creates minHeap 
        
        totalSum = 0
        for i in nums:
            # Adding items to the heap using heappush
            # for maxHeap, function by multiplying them with -1
            heappush(maxHeap, -1*i) 
            totalSum += i
        
        requiredSum = totalSum / 2
        minOps = 0
        
        while totalSum > requiredSum:
            x = -1*heappop(maxHeap) # Got negative value make it positive
            x /= 2
            totalSum -= x
            heappush(maxHeap, -1*x) 
            minOps += 1
        
        return minOps