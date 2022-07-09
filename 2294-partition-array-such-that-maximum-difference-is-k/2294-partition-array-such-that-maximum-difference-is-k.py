class Solution:
    # def partitionArray(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     n=len(nums)
    #     i=0
    #     j=0
    #     counti=0
    #     while j<n and i<n:
    #         if nums[j]-nums[i]<=k:
    #             j+=1
    #         else:
    #             counti+=1
    #             i=j
    #     return counti+1        
    def partitionArray(self, A, k):
        A.sort()
        res = 1
        mn = mx = A[0]
        for a in A:
            mn = min(mn, a)
            mx = max(mx, a)
            if mx - mn > k:
                res += 1
                mn = mx = a
        return res
