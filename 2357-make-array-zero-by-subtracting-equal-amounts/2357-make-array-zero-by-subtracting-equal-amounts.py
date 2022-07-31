class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        counti=1
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                counti+=1
        if nums[0]==0:
            return counti-1
        return counti