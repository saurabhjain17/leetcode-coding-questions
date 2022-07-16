import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        n=len(nums)
        sumi=sum(nums)
        sumi_want=sumi
        for i in range(n):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        counti=0
        while sumi_want*2>sumi:
            counti+=1
            number=-heapq.heappop(nums)
            sumi_want-=number
            number/=2
            sumi_want+=number
            heapq.heappush(nums,-number)
        return counti    