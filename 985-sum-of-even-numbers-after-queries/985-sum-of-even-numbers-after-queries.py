class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumi=0
        n=len(nums)
        ans=[]
        for i in nums:
            if i%2==0:
                sumi+=i
        for u,v in queries:
            if nums[v]%2==0:
                sumi-=nums[v]
            nums[v]+=u
            if nums[v]%2==0:
                sumi+=nums[v]
            ans.append(sumi)
        return ans    