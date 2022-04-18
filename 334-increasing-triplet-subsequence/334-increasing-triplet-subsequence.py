class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fir=sec=float("-inf")
        fir=nums[0]
        n=len(nums)
        i=1
        while i<n and sec==float("-inf"):
            if nums[i]<=fir:
                fir=nums[i]
            else:
                sec=nums[i]
            i+=1
        if i==n:
            return False
        while i<n:
            if nums[i]>sec:
                return True
            elif nums[i]>fir :
                sec=nums[i]
            else:
                fir=nums[i]
            i+=1
        return False    
        