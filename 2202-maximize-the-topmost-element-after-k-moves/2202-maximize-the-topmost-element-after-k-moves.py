class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k==0:
            return nums[0]
        n=len(nums)
        if n==1:
            if k%2==1:
                return -1
            return nums[0]
        t=k-1
        if t==0:
            return nums[1]
        if k>n:
            return max(nums)
        maxi=max(nums[:t])
        if t==n-1:
            return maxi
        else:
            return max(maxi,nums[t+1])