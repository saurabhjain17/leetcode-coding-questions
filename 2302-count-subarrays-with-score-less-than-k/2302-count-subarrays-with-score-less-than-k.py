class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        counti=0
        sumi=[0]*(n+1)
        for i in range(1,n+1):
            sumi[i]=sumi[i-1]+nums[i-1]
        for i in range(1,n+1):
            if nums[i-1]<k:
                low=i
                high=n
                ans=i
                while low<=high:
                    mid=(low+high)//2
                    prod=(sumi[mid]-sumi[i-1])*(mid-i+1)
                    if prod<k:
                        ans=mid
                        low=mid+1
                    else:
                        high=mid-1
                counti+=ans-i+1
        return counti        