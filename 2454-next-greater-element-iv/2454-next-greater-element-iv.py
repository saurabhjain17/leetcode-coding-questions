class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        fir_greater=[n]*n
        s=[n-1]
        for i in range(n-2,-1,-1):
            while s and nums[s[-1]]<=nums[i]:
                s.pop(-1)
            if s:
                fir_greater[i]=s[-1]
            s.append(i)
        ans=[-1]*n    
        for i in range(n):
            l=fir_greater[i]+1
            while l<n and nums[i]>=nums[l]:
                 l=fir_greater[l]
            if l>=n:
                ans[i]=-1
            else:
                ans[i]=nums[l]
        return ans        