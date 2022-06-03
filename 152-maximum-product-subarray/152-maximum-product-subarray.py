class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        n=len(nums)
        prod=1
        for i in nums:
            if i==0:
                maxi=max(maxi,0)
                prod=1
            else:
                prod*=i
                maxi=max(maxi,prod)
        prod=1        
        for i in range(n-1,-1,-1)  :      
            if nums[i]==0:
                prod=1
            else:
                prod*=nums[i]
                maxi=max(maxi,prod)
        return maxi        