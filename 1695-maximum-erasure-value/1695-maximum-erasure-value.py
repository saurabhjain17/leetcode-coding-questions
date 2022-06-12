class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        seti=set()
        i=0
        j=0
        sumi=0
        while j<n and i<=j:
            if nums[j] not in seti:
                seti.add(nums[j])
                sumi+=nums[j]
                maxi=max(sumi,maxi)
                j+=1
            elif nums[j]==nums[i]:
                maxi=max(sumi,maxi)
                i+=1
                j+=1
            else:
                sumi-=nums[i]
                seti.discard(nums[i])
                i+=1
        return max(maxi,sumi)        