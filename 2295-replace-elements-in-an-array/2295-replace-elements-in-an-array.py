class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic=dict()
        n=len(nums)
        for i in range(n):
            dic[nums[i]]=i
        for u,v in operations:
            nums[dic[u]]=v
            dic[v]=dic[u]
        return nums    